import tkinter as tk

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


def main():
    myApp = tk.Tk()
    myApp.geometry("400x400")
    myApp.title("Student Viewer")

    frame1 = tk.LabelFrame(myApp, text="Menu", background="cyan", height=50, width=200)
    frame1.grid(row=0, column=0, sticky="nsew")

    frames = make_frames(myApp)
    myApp.mainloop()

main()
