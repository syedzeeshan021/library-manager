import streamlit as st
import json
import pandas as pd
from datetime import datetime
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="Personal Library Manager", layout="wide", initial_sidebar_state="expanded")

# File to store library data
LIBRARY_FILE = "library.txt"

def load_library():
    """Load the library from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save the library to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Use Streamlit session state to persist library data
if "library" not in st.session_state:
    st.session_state.library = load_library()

# Sidebar Navigation
menu_option = st.sidebar.radio(
    "📚 Navigation",
    [
        "🏠 Home",
        "➕ Add Book",
        "🗑️ Remove Book",
        "🔍 Search Book",
        "📖 Display Library",
        "📊 Statistics",
        "⬇️ Download Library",
    ],
)

# Home Page with instructions and a welcome message
if menu_option == "🏠 Home":
    st.title("Welcome to Your Personal Library Manager!")
    st.subheader("It is an interactive Streamlit-based web application that lets you manage your personal book collection in a dynamic and user-friendly way. You can add, remove, search, display, and analyze your library—all with a modern UI, clear instructions, and fun emojis.")
    st.header("📖 Instructions")
    st.markdown(
        """
        - **Add a Book:** Use the "➕ Add Book" option to add a new book to your library.
        - **Remove a Book:** Use the "🗑️ Remove Book" option to remove a book from your library.
        - **Search Book:** Use the "🔍 Search Book" option to find books by title or author.
        - **Display Library:** Use the "📖 Display Library" option to view all your books in a table.
        - **Statistics:** Use the "📊 Statistics" option to see summary statistics of your library.
        - **Download Library:** Use the "⬇️ Download Library" option to export your library data as an Excel file.

        **Enjoy managing your books! 😊**
        """
    )

elif menu_option == "➕ Add Book":
    st.header("➕ Add a New Book")
    with st.form("add_book_form"):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Title", placeholder="e.g., The Great Gatsby")
            author = st.text_input("Author", placeholder="e.g., F. Scott Fitzgerald")
            year = st.text_input("Publication Year", value=str(datetime.now().year))
        with col2:
            genre = st.text_input("Genre", placeholder="e.g., Fiction")
            read = st.selectbox("Have you read it?", ["Yes", "No"])
        submit = st.form_submit_button("Add Book")
        if submit:
            try:
                year_int = int(year)
            except ValueError:
                year_int = 0
            book = {
                "title": title,
                "author": author,
                "year": year_int,
                "genre": genre,
                "read": True if read == "Yes" else False,
            }
            st.session_state.library.append(book)
            save_library(st.session_state.library)
            st.success("✅ Book added successfully!")

elif menu_option == "🗑️ Remove Book":
    st.header("🗑️ Remove a Book")
    if st.session_state.library:
        titles = [book["title"] for book in st.session_state.library]
        book_to_remove = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            for book in st.session_state.library:
                if book["title"] == book_to_remove:
                    st.session_state.library.remove(book)
                    save_library(st.session_state.library)
                    st.success("✅ Book removed successfully!")
                    break
    else:
        st.info("Your library is empty.")

elif menu_option == "🔍 Search Book":
    st.header("🔍 Search for a Book")
    if st.session_state.library:
        search_by = st.radio("Search by", ["Title", "Author"])
        query = st.text_input("Enter your search query", placeholder="Type here...")
        if st.button("Search"):
            if search_by == "Title":
                results = [book for book in st.session_state.library if query.lower() in book["title"].lower()]
            else:
                results = [book for book in st.session_state.library if query.lower() in book["author"].lower()]
            if results:
                st.subheader("Matching Books")
                df_results = pd.DataFrame(results)
                st.dataframe(df_results)
            else:
                st.warning("⚠️ No matching books found.")
    else:
        st.info("Your library is empty.")

elif menu_option == "📖 Display Library":
    st.header("📖 Your Library")
    if st.session_state.library:
        df = pd.DataFrame(st.session_state.library)
        st.dataframe(df)
    else:
        st.info("Your library is empty.")

elif menu_option == "📊 Statistics":
    st.header("📊 Library Statistics")
    if st.session_state.library:
        total = len(st.session_state.library)
        read_count = sum(1 for book in st.session_state.library if book["read"])
        percent_read = (read_count / total * 100) if total > 0 else 0
        st.markdown(f"**Total Books:** {total}")
        st.markdown(f"**Books Read:** {read_count}")
        st.markdown(f"**Percentage Read:** {percent_read:.2f}%")
    else:
        st.info("Your library is empty.")

elif menu_option == "⬇️ Download Library":
    st.header("⬇️ Download Library Data")
    if st.session_state.library:
        df = pd.DataFrame(st.session_state.library)
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Library")
        buffer.seek(0)
        st.download_button(
            label="Download as Excel",
            data=buffer,
            file_name="library.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    else:
        st.info("Your library is empty.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by [Syed Zeeshan Iqbal]")

