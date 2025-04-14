import requests
import random

GOOGLE_BOOKS_API = "AIzaSyBCrGS2jiNceAlJDOqsBWMzJCVbmJGPVLQ"

mood_genre = {
    "Happy": ["humor", "feel-good"],
    "Sad": ["tragedy", "drama", "inspirational", "healing"],
    "Angry": ["action", "adventure", "thriller"],
    "Adventurous": ["adventure", "action", "fantasy"],
    "Romantic": ["romance", "love", "relationship"],
    "Curious": ["mystery", "suspense", "thriller"],
    "Nostalgic": ["historical", "classic", "nostalgia"],
    "Relaxed": ["self-help", "personal development", "spiritual"],
    "Motivated": ["self-help", "personal development", "inspirational"]
}

def get_book_by_mood(mood):
    if mood:
        keywords = mood_genre.get(mood, ["fiction"])
        keyword = random.choice(keywords)
    else:
        keyword = random.choice(["fiction", "non-fiction", "mystery", "fantasy", "romance"])

    params = {
        "q": keyword,
        "maxResults": 10,
        "printType": "books",
        "key": GOOGLE_BOOKS_API
    }

    response = requests.get("https://www.googleapis.com/books/v1/volumes", params=params)

    if response.status_code == 200:
        items = response.json().get("items", [])
        if items:
            book = random.choice(items)
            info = book.get("volumeInfo", {})
            return {
                "title": info.get("title", "Unknown Title"),
                "author": ", ".join(info.get("authors", ["Unknown Author"])),
                "description": info.get("description", "No description available."),
                "thumbnail": info.get("imageLinks", {}).get("thumbnail", ""),
                "preview_link": info.get("previewLink", "")
            }
    return {"error": "No books found."}
