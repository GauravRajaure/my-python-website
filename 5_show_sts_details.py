import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


def quit(myApp):
    answer = messagebox.askquestion("Confirm", "Are you sure you want to quit?")
    if answer == "yes":
        myApp.destroy()
    else:
        messagebox.showinfo("Information", "Keep Going!")


def make_frames(root):
    frames = {
        "menu": tk.LabelFrame(root, text="Menu", background="cyan", height=50, width=200),
        "images": tk.LabelFrame(root, text="Images", background="teal", height=100, width=200),
        "details": tk.LabelFrame(root, text="Details", background="pink", height=100, width=200),
        "final": tk.LabelFrame(root, text="Final", background="green", height=100, width=200),
    }

    frames["menu"].grid(row=0, column=0, sticky="nsew", columnspan=2)
    frames["images"].grid(row=1, column=0, sticky="nsew")
    frames["details"].grid(row=1, column=1, sticky="nsew")
    frames["final"].grid(row=3, column=0, sticky="nsew")
    
    return frames


def make_buttons(root, frames, students):
    buttons = {
        "show": ttk.Button(
            frames["menu"], text="Show Students", command= lambda: show_students(frames, students)),
        "clear": ttk.Button(frames["menu"], text="Clear", command= lambda: clear_all_frames(frames)),
        "quit": ttk.Button(frames["menu"], text="Quit", command= lambda: quit(root)),
    }
    
    col = 0
    for button in buttons.values():
        button.grid(row=0, column=col, sticky="nsew")
        col += 1

    return buttons


def show_students(frames, students):
    row = 0
    col = 0
    for student in students:
        image = Image.open(student["image"])
        image = image.resize((70, 70), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        btn = ttk.Button(frames["images"], image=photo, command= lambda s=student: show_info(frames, s))
        btn.image = photo  # keep reference
        btn.grid(row=row, column=col)
        col += 1
        if col % 3 == 0:
            col = 0
            row += 1


def clear_all_frames(frames):
    for frame_name, frame in frames.items():
        if frame_name != "menu": 
            for widget in frame.winfo_children():
                widget.destroy()


def show_info(frames, student):
    clear_all_frames({"details": frames["details"]})
    name_label = ttk.Label(frames["details"], text=f"Name: {student['name']}", font=("Arial", 12))
    age_label = ttk.Label(frames["details"], text=f"Age: {student['age']}", font=("Arial", 12))
    major_label = ttk.Label(frames["details"], text=f"Major: {student['major']}", font=("Arial", 12))

    name_label.pack(anchor="w", pady=5)
    age_label.pack(anchor="w", pady=5)
    major_label.pack(anchor="w", pady=5)


def main():
    myApp = tk.Tk()
    myApp.geometry("400x400")
    myApp.title("Student Viewer")

    students = [
        {"name": "Alice", "age": 20, "major": "Computer Science", "image": "img/alice.jpg"},
        {"name": "Bob", "age": 21, "major": "Mathematics", "image": "img/bob.png"},
        {"name": "Charlie", "age": 22, "major": "Physics", "image": "img/charlie.png"},
        {"name": "Diana", "age": 23, "major": "Chemistry", "image": "img/diana.jpg"}
    ]

    frames = make_frames(myApp)
    make_buttons(myApp, frames, students)

    myApp.mainloop()

main()
