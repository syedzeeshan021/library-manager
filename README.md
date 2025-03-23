# Personal Library Manager 📚
Personal Library Manager is an interactive Streamlit-based web application that lets you manage your personal book collection in a dynamic and user-friendly way. You can add, remove, search, display, and analyze your library—all with a modern UI, clear instructions, and fun emojis.

## Features
# Add Books:
Easily add books to your library with details such as title, author, publication year, genre, and read status.

# Remove Books:
Remove any book from your collection using an intuitive selection interface.

# Search Books:
Quickly search for books by title or author with real-time filtering.

# Display Library:
View all your books in an interactive table that supports scrolling and sorting.

# Statistics:
Get an overview of your collection with summary statistics, including total books, books read, and percentage read.

# Download Library:
Export your entire library as an Excel file with a single click.

# Interactive & User-Friendly UI:
Enjoy a clean, modern interface with clear navigation, friendly instructions, and engaging emojis.

## Installation
# Clone the Repository

git clone https://github.com/yourusername/personal-library-manager.git
cd personal-library-manager

# Install Dependencies:

pip install -r requirements.txt
Ensure your requirements.txt file includes:

streamlit
pandas
openpyxl

## Usage
# Run the Application:

# Start the Streamlit app by running:

streamlit run app.py
Interact with the App:

# Navigation:
Use the sidebar to choose different functionalities like adding a book, removing a book, searching, viewing your library, checking statistics, and downloading data.

# Adding a Book:
Fill out the form with the book's details and click "Add Book" to save it.

# Searching & Removing Books:
Use the provided controls to search or remove books from your collection.

# Download Option:
Click the download button to export your library as an Excel file.

# Project Structure
app.py
The main Streamlit application file containing all the UI code and library management logic.

library.txt
The file used to store your library data in JSON format.

requirements.txt
Contains the list of required Python packages.

# Contributing
Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss your ideas.

# Acknowledgments
Streamlit for making it easy to build interactive data apps.

Pandas for robust data manipulation.

The developer community for their continuous support and contributions.
