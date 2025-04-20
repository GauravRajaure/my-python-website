import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Styled Buttons")
root.geometry("400x100")

# Define a common style
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("Disabled.TButton", font=("Arial", 12), padding=10, foreground="gray")

# Frame to hold buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

# Create and pack buttons using a loop
for i in range(4):
    if i == 2:  # Make the third button disabled
        btn = ttk.Button(button_frame, text=f"Button {i+1}", style="Disabled.TButton", state="disabled")
    else:
        btn = ttk.Button(button_frame, text=f"Button {i+1}", style="TButton")
    btn.pack(side=tk.LEFT, padx=5)

root.mainloop()