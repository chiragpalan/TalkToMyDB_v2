import streamlit as st
from ui_helpers import display_erd
from db_helpers import ask_question

# Streamlit app configuration
st.set_page_config(page_title="Sakila Database Explorer", layout="wide")

# Title and description
st.title("🎥 Sakila Database Explorer")
st.markdown("""
This app allows you to interact with the Sakila database using natural language queries.
- View the **ERD diagram** of the database.
- Ask questions about the database, and get SQL-generated answers.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to:", ["ERD Diagram", "Ask a Question"])

if option == "ERD Diagram":
    st.header("Entity-Relationship Diagram (ERD)")
    display_erd()

elif option == "Ask a Question":
    st.header("Ask a Question")
    question = st.text_input("Enter your question:")
    if st.button("Submit"):
        if question.strip():
            result = ask_question(question)
            st.subheader("Generated SQL Query")
            st.code(result["sql"], language="sql")
            st.subheader("Query Results")
            st.dataframe(result["df"])
        else:
            st.warning("Please enter a valid question.")
