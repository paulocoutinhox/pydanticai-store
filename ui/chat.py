import asyncio

import streamlit as st

from ai.bookstore_agent import (
    BookstoreDependencies,
    bookstore_agent,
    extract_contact_info,
    process_purchase,
)


async def process_purchase_success(
    prompt: str, order: dict, email: str, deps: BookstoreDependencies
) -> str:
    """Let the AI generate a natural success message"""
    success_context = f"Purchase completed successfully. Order ID: {order['id']}, Email: {email}, Amount: ${order['price']:.2f}. Generate a friendly success message in the same language as: {prompt}"

    result = await bookstore_agent.run(success_context, deps=deps)
    return result.output.response


def render_chat():
    """Renders the main chat interface"""
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Type your message..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Process agent response
        with st.chat_message("assistant"):
            with st.spinner("Processing..."):
                try:
                    # Create dependencies
                    deps = BookstoreDependencies(
                        db=st.session_state.db,
                        email_service=st.session_state.email_service,
                    )

                    # Check if user provided contact info and there's a pending purchase
                    if st.session_state.current_order:
                        email, phone = extract_contact_info(prompt)
                        if email and phone:
                            # Process the pending purchase
                            try:
                                order = asyncio.run(
                                    process_purchase(
                                        ctx=None,
                                        book_id=st.session_state.current_order[
                                            "book_id"
                                        ],
                                        email=email,
                                        phone=phone,
                                    )
                                )

                                if order:
                                    # Let AI generate natural success message
                                    response = asyncio.run(
                                        process_purchase_success(
                                            prompt, order, email, deps
                                        )
                                    )
                                    st.session_state.current_order = None
                                else:
                                    response = "Sorry, there was an error processing your purchase. Please try again."
                            except Exception as e:
                                response = f"Sorry, an error occurred: {str(e)}"
                        else:
                            # Continue with normal agent processing
                            response = asyncio.run(process_with_agent(prompt, deps))
                    else:
                        # Normal processing without pending purchase
                        response = asyncio.run(process_with_agent(prompt, deps))

                    st.markdown(response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )

                except Exception as e:
                    error_msg = f"Sorry, an error occurred: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_msg}
                    )


async def process_with_agent(prompt: str, deps: BookstoreDependencies) -> str:
    """Process user input with the AI agent"""
    # Build conversation context
    context_prompt = prompt
    if st.session_state.conversation_context:
        context_prompt = f"Previous context: {' | '.join(st.session_state.conversation_context[-3:])}\n\nCurrent question: {prompt}"

    # Run agent
    result = await bookstore_agent.run(context_prompt, deps=deps)

    # Update conversation context
    st.session_state.conversation_context.append(f"User: {prompt}")
    st.session_state.conversation_context.append(f"Assistant: {result.output.response}")

    # Keep only the last 10 interactions to avoid overload
    if len(st.session_state.conversation_context) > 20:
        st.session_state.conversation_context = st.session_state.conversation_context[
            -20:
        ]

    # Handle purchase flow
    if result.output.action == "process_purchase" and result.output.needs_contact:
        st.session_state.current_order = {
            "book_id": result.output.book_id,
            "price": result.output.price,
        }

    # Return the AI's natural response
    return result.output.response
