import tkinter as tk
from tkinter import ttk, messagebox

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


def make_buttons(root, frames):
    buttons = {
        "show": ttk.Button(
            frames["menu"], text="Show Students"),
        "clear": ttk.Button(frames["menu"], text="Clear", command=""),
        "quit": ttk.Button(frames["menu"], text="Quit", command= lambda: quit(root)),
    }
    
    col = 0
    for button in buttons.values():
        button.grid(row=0, column=col, sticky="nsew")
        col += 1

    return buttons

def main():
    myApp = tk.Tk()
    myApp.geometry("400x400")
    myApp.title("Student Viewer")

    frames = make_frames(myApp)
    make_buttons(myApp, frames)

    myApp.mainloop()

main()
