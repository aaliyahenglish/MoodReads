import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from fetching_books import get_book_by_mood

def save_to_reading_log(book):
    with open("reading_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{book['title']} by {book['author']}\n")
        f.write(f"Preview: {book['preview_link']}\n")
        f.write("-" * 40 + "\n")

def recommend_book(mood=None):
    book = get_book_by_mood(mood)
    if "error" in book:
        messagebox.showerror("Error", book["error"])
        return

    title_label.config(text=book['title'])
    author_label.config(text=f"By {book['author']}")
    description_text.delete(1.0, tk.END)
    description_text.insert(tk.END, book["description"])

    if book["thumbnail"]:
        img_data = requests.get(book["thumbnail"]).content
        img = Image.open(BytesIO(img_data)).resize((100, 150))
        cover_img = ImageTk.PhotoImage(img)
        cover_label.config(image=cover_img)
        cover_label.image = cover_img
    else:
        cover_label.config(image="", text="Cover not available")

    # Save to reading log
    save_to_reading_log(book)

root = tk.Tk()
root.title("Mood-Based Book Recommender")
root.geometry("420x550")

# Mood dropdown
mood_var = tk.StringVar()
moods = ["Happy", "Sad", "Angry", "Adventurous", "Romantic", "Curious", "Nostalgic", "Relaxed", "Motivated"]
mood_dropdown = tk.OptionMenu(root, mood_var, *moods)
mood_dropdown.config(font=("Arial", 12))
mood_var.set("Happy")
mood_dropdown.pack(pady=10)

# Buttons
recommend_button = tk.Button(root, text="Recommend Book", font=("Arial", 12),
                             command=lambda: recommend_book(mood_var.get()))
recommend_button.pack(pady=5)

surprise_button = tk.Button(root, text="Surprise Me!", font=("Arial", 12),
                            command=lambda: recommend_book())
surprise_button.pack(pady=5)

# Book info
title_label = tk.Label(root, text="", font=("Arial", 14, "bold"), wraplength=380, justify="center")
title_label.pack(pady=10)

author_label = tk.Label(root, text="", font=("Arial", 12))
author_label.pack(pady=5)

cover_label = tk.Label(root)
cover_label.pack(pady=10)

description_text = tk.Text(root, height=6, wrap=tk.WORD, font=("Arial", 10))
description_text.pack(pady=10)

root.mainloop()
