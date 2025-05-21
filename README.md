# MoodReads 📚 
Don't know what to read? Well, let's find a mood-based book recommender that helps you pick your next read based on your feelings. Whether you're happy, sad, or just want a surprise, this app has a book for you. Powered by the Google Books API.

### Created By: Aaliyah English



## ✨ Features 

- Choosing a mood from a dropdown menu
- Get a random book recommendation based on that mood 
- "Surprise Me" option/button for random genre-based suggestions
- View book, title, author, description, and cover
- Save recommendations to a local file called "reading_log.txt" file


## Requirements 

- Python
- Pillow 'pip install pillow'
- Requests 'pip install requests'

## Steps

1. Define the Project Idea
  I wanted to build an app that helps users find book recommendations based on their mood.

2. Choosing an API
   Originally, I was going to use GoodReadsAPI, but I ran into a few difficulties. So I came across GoogleBooksAPI to fetch live book data like titles, authors, covers, and descriptions.

3. Moods -> Genres
   I created a Python dictionary to connect different moods (e.g., "happy", "sad") to relevant genres (e.g., "humor", "tragedy"). Created Core Python Files

4. Created Python Files

    ✅Book_fetching.py: Logic for API requests and book data parsing.

    ✅Moodbooks_gui.py: Built the GUI using Tkinter for user interaction.

    ✅Reading_log.txt: Used to store a log of recommended books.

    ✅Requirements.txt: Added to manage and list all Python dependencies.

5. Implemented the Book Fetching Functionality
   Built get_book_by_mood() to choose genres and retrieve matching books from the API.
  Included error handling for cases when no books are found.

6. Developed the Graphical User Interface
    Added dropdown for moods, “Recommend Book” and “Surprise Me!” buttons.
    Displayed book info (title, author, description) and cover image using Pillow

7. Added Reading Log Functionality
    Appended recommended books (title, author, preview link) to reading_log.txt after each recommendation.

# Final Version

https://github.com/user-attachments/assets/54cbf23b-10fe-4799-b5f2-0b03e4ee26ee

