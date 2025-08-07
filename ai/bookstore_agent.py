import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

from data.db import BookDatabase
from helper.email_service import EmailService


# Dependencies for the agent
@dataclass
class BookstoreDependencies:
    db: BookDatabase
    email_service: EmailService


# Structured output model
class BookstoreOutput(BaseModel):
    response: str = Field(
        description="Friendly response to the customer about books or store information. Use the context of the previous conversation when relevant. IMPORTANT: Always respond in the same language that the customer is using. We sell theological books in PDF format only.",
        min_length=10,
        max_length=1000,
    )
    action: str = Field(
        description="Action to be taken: 'search_books', 'book_details', 'process_purchase', 'list_popular', 'help', 'extract_contact'",
        pattern=r"^(search_books|book_details|process_purchase|list_popular|help|extract_contact)$",
    )
    book_id: Optional[str] = Field(description="Book ID if relevant", default=None)
    needs_contact: bool = Field(
        description="If email/phone is needed to complete the action"
    )
    price: Optional[float] = Field(description="Book price if relevant", default=None)
    email: Optional[str] = Field(
        description="Extracted email from user message", default=None
    )
    phone: Optional[str] = Field(
        description="Extracted phone from user message", default=None
    )


# Bookstore agent
bookstore_agent = Agent(
    "google-gla:gemini-2.5-flash",
    deps_type=BookstoreDependencies,
    output_type=BookstoreOutput,
    system_prompt=(
        "You are a virtual assistant for an online bookstore specialized in theological books in PDF format. "
        "CRITICAL: Always detect the language the customer is using and respond in the SAME language. "
        "If they write in Portuguese, respond in Portuguese. If they write in English, respond in English. "
        "If they write in Spanish, respond in Spanish. And so on for any other language. "
        "Be friendly, helpful, and adapt your communication style to the customer's language and culture. "
        "Help customers find books, provide details, process purchases, and answer questions. "
        "Always be enthusiastic about books and offer suggestions when appropriate. "
        "Keep the conversation context and remember what the customer has already asked or purchased. "
        "When a customer provides email and phone information, extract them and use action 'extract_contact'. "
        "If there's a pending purchase and contact info is provided, process the purchase immediately. "
        "IMPORTANT: When customers ask 'what is [book name]' or 'what does [book name] cover' or similar questions, "
        "ALWAYS use the 'get_book_details' tool to get the complete description and use that information in your response. "
        "The description contains detailed information about what the book covers and its content. "
        "Never say you couldn't find details - always search for the book and use its description. "
        "IMPORTANT: When customers ask about popular books, best sellers, or most popular titles, "
        "ALWAYS use the 'list_popular_books' tool and include the results in your response. "
        "Format the books nicely with emojis, ratings, prices, and descriptions. "
        "IMPORTANT: When a purchase requires contact information, generate a natural, friendly request "
        "asking for email and phone in the customer's language. Do not use placeholders or technical terms. "
        "Make it sound conversational and helpful. "
        "NOTE: We only sell books in PDF format. Do not mention audiobooks or ebooks in other formats. "
        "Remember: Language detection and matching is your top priority!"
    ),
)


# Agent tools
@bookstore_agent.tool
async def search_books(
    ctx: RunContext[BookstoreDependencies], query: str
) -> List[Dict[str, Any]]:
    """Search books by title, author, or category"""
    return ctx.deps.db.search_books(query)


@bookstore_agent.tool
async def get_book_details(
    ctx: RunContext[BookstoreDependencies], book_id: str
) -> Optional[Dict[str, Any]]:
    """Get complete details of a specific book. Can search by ID, title, or partial title match."""
    # First try direct ID lookup
    book = ctx.deps.db.get_book_details(book_id)
    if book:
        return book

    # If not found by ID, search by title or partial title
    search_results = ctx.deps.db.search_books(book_id)
    if search_results:
        # Return the first (most relevant) result
        return search_results[0]

    return None


@bookstore_agent.tool
async def list_popular_books(
    ctx: RunContext[BookstoreDependencies], limit: int = 5
) -> List[Dict[str, Any]]:
    """List the most popular books in the store"""
    return ctx.deps.db.get_popular_books(limit)


@bookstore_agent.tool
async def process_purchase(
    ctx: RunContext[BookstoreDependencies], book_id: str, email: str, phone: str
) -> Dict[str, Any]:
    """Process the purchase of a book"""
    order = ctx.deps.db.create_order(book_id, email, phone)
    if order:
        ctx.deps.email_service.send_purchase_confirmation(order)
    return order


@bookstore_agent.tool
async def get_conversation_history(
    ctx: RunContext[BookstoreDependencies],
) -> List[Dict[str, Any]]:
    """Returns the current conversation history"""
    # This tool allows the agent to access history when needed
    return [
        {
            "type": "tool",
            "description": "Conversation history available for context",
            "interactions": 0,  # This will be updated by the UI
        }
    ]


def extract_contact_info(text: str) -> tuple[Optional[str], Optional[str]]:
    """Extract email and phone from text"""
    # Email regex pattern
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_match = re.search(email_pattern, text)
    email = email_match.group() if email_match else None

    # Phone regex pattern (various formats)
    phone_pattern = r"(\+?1?[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})"
    phone_match = re.search(phone_pattern, text)
    phone = "".join(phone_match.groups()[1:]) if phone_match else None

    return email, phone
