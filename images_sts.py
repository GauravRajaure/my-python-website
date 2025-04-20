import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Sample student data
students = [
    {"name": "Alice", "age": 20, "major": "Computer Science", "image": "img/alice.jpg"},
    {"name": "Bob", "age": 21, "major": "Mathematics", "image": "img/bob.png"},
    {"name": "Charlie", "age": 22, "major": "Physics", "image": "img/charlie.png"},
    {"name": "Diana", "age": 23, "major": "Chemistry", "image": "img/diana.jpg"}
]

# Create main window
root = tk.Tk()
root.title("Student Viewer")
root.geometry("600x400")

# Frames for layout
image_frame = ttk.Frame(root, padding=10)
image_frame.grid(row=0, column=0, sticky="n")
info_frame = ttk.Frame(root, padding=10)
info_frame.grid(row=0, column=1, sticky="n")

# Info labels
name_label = ttk.Label(info_frame, text="Name: ", font=("Arial", 12))
age_label = ttk.Label(info_frame, text="Age: ", font=("Arial", 12))
major_label = ttk.Label(info_frame, text="Major: ", font=("Arial", 12))

name_label.pack(anchor="e", pady=5)
age_label.pack(anchor="e", pady=5)
major_label.pack(anchor="e", pady=5)

# Function to display student info
def show_info(student):
    name_label.config(text=f"Name: {student['name']}")
    age_label.config(text=f"Age: {student['age']}")
    major_label.config(text=f"Major: {student['major']}")

# Load and display student image buttons
for student in students:
    image = Image.open(student["image"])
    image = image.resize((70, 70), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    btn = ttk.Button(image_frame, image=photo, command=lambda s=student: show_info(s))
    btn.image = photo  # keep reference
    btn.pack(pady=5)

root.mainloop()
