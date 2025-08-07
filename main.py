import streamlit as st

from data.db import BookDatabase
from helper.email_service import EmailService
from ui.chat import render_chat


def main():
    st.set_page_config(page_title="📚 Virtual Bookstore", page_icon="📚", layout="wide")

    st.title("📚 Virtual Bookstore")
    st.markdown("---")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "db" not in st.session_state:
        st.session_state.db = BookDatabase()

    if "email_service" not in st.session_state:
        st.session_state.email_service = EmailService()

    if "current_order" not in st.session_state:
        st.session_state.current_order = None

    # Initialize conversation context
    if "conversation_context" not in st.session_state:
        st.session_state.conversation_context = []

    # Main chat area
    render_chat()


if __name__ == "__main__":
    main()
