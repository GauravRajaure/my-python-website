# Import necessary modules from tkinter
import tkinter as tk
from tkinter import ttk

# Create a tkinter application instance
myApp = tk.Tk()

# Configure the main application window
myApp.geometry("400x300")  # Set the dimensions of the window
myApp.configure(background="LightBlue2")  # Set the background color
myApp.resizable(True, True)  # Allow the window to be resizable
myApp.title("ttk Styles in Action")  # Set the title of the window

# Section 1: Define all styles in one place
style = ttk.Style()
style.theme_use('alt')  # Use the 'alt' theme for ttk widgets

# Style for a standard tk.Label with relief and border
standard_label_style = {
    "bg": "cyan",  # Background color
    "foreground":'black',  # Text color
    "width": 20,
    "height": 2,
    "relief": tk.RAISED,  # Relief effect
    "borderwidth": 2  # Border width to make the relief visible
}

# Custom style for ttk labels
style.configure(
    'Custom.TLabel',
    background='red',  # Background color
    foreground='yellow',  # Text color
    borderwidth=10,  # Border width
    width=20,
    height=2,
    relief=tk.GROOVE  # Relief effect
)

# Style for a heading label
style.configure(
    'Heading.TLabel',
    background='green',  # Background color
    foreground='blue',  # Text color
    width=20,
    height=2,
    font=('Helvetica', 15),  # Font style and size
    relief=tk.FLAT  # No relief effect
)

# Another custom style for ttk labels
style.configure(
    'Custom2.TLabel',
    background='blue',  # Background color
    foreground='white',  # Text color
    width=20,
    height=2,
    font=('Helvetica', 12),  # Font style and size
    relief=tk.RAISED,  # Relief effect
    borderwidth=2  # Border width
)

# Section 2: Create all labels in one place
# Standard tk.Label without ttk styles
labelTitle = tk.Label(myApp, text="Label without style", **standard_label_style)
labelTitle.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# ttk.Label with custom style
labelTitle1 = ttk.Label(myApp, text="Label with style", style='Custom.TLabel')
labelTitle1.grid(row=4, column=0, columnspan=4, padx=10, pady=20)

# ttk.Label with heading style
labelTitle2 = ttk.Label(myApp, text="Label with heading style", style='Heading.TLabel')
labelTitle2.grid(row=6, column=0, columnspan=4, padx=10, pady=20)

# ttk.Label with another custom style
labelTitle3 = ttk.Label(myApp, text="Another Label with custom style", style='Custom2.TLabel')
labelTitle3.grid(row=8, column=0, columnspan=4, padx=10, pady=20)

# Section 3: Adjust padding and alignment for all child widgets
# Loop through all child widgets and configure their grid settings
for item in myApp.winfo_children():
    item.grid_configure(
        padx=10,  # Horizontal padding
        pady=10,  # Vertical padding
        ipadx=10,  # Internal horizontal padding
        ipady=10,  # Internal vertical padding
        sticky=tk.SW  # Align widgets to the bottom-left (South-West)
    )

# Start the tkinter event loop
myApp.mainloop()