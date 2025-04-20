import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Sample student data
students = [
    {"name": "Alice", "age": 20, "major": "Computer Science", "image": "img/alice.jpg"},
    {"name": "Bob", "age": 21, "major": "Mathematics", "image": "img/bob.png"},
    {"name": "Charlie", "age": 22, "major": "Physics", "image": "img/charlie.png"},
    {"name": "Diana", "age": 23, "major": "Chemistry", "image": "img/diana.jpg"},
    {"name": "Eve", "age": 24, "major": "Biology", "image": "img/eve.jpg"},
    {"name": "Frank", "age": 25, "major": "Economics", "image": "img/frank.jpg"},
    {"name": "Grace", "age": 26, "major": "Art", "image": "img/grace.jpg"},
    {"name": "Henry", "age": 27, "major": "Engineering", "image": "img/henry.jpg"}
]

# Create main window
root = tk.Tk()
root.title("Student Viewer")
root.geometry("800x400")

# Frames for layout with background colors
image_frame = tk.Frame(root, bg="#e0f7fa", padx=10, pady=10)
image_frame.grid(row=0, column=0, sticky="n")
info_frame = tk.Frame(root, bg="#fff3e0", padx=10, pady=10)
info_frame.grid(row=0, column=1, sticky="n")

# Info labels
name_label = tk.Label(info_frame, text="Name: ", font=("Arial", 12), bg="#fff3e0")
age_label = tk.Label(info_frame, text="Age: ", font=("Arial", 12), bg="#fff3e0")
major_label = tk.Label(info_frame, text="Major: ", font=("Arial", 12), bg="#fff3e0")

name_label.pack(anchor="w", pady=5)
age_label.pack(anchor="w", pady=5)
major_label.pack(anchor="w", pady=5)

# Function to display student info
def show_info(student):
    name_label.config(text=f"Name: {student['name']}")
    age_label.config(text=f"Age: {student['age']}")
    major_label.config(text=f"Major: {student['major']}")

# Load and display student image buttons in a 4-column layout
columns = 4
for index, student in enumerate(students):
    row = index // columns
    col = index % columns

    image = Image.open(student["image"])
    image = image.resize((70, 70), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    btn = ttk.Button(image_frame, image=photo, command=lambda s=student: show_info(s))
    btn.image = photo  # keep reference
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
