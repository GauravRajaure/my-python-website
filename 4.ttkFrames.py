# Import necessary modules from tkinter
from tkinter import *
from tkinter import ttk

# Create a tkinter window instance
myApp = Tk()

# Set the dimensions of the window
myApp.geometry("500x500")

# Set the background color of the window
myApp.configure(background="LightBlue2")

# Allow the window to be resizable
myApp.resizable("true", "true")

# Set the title of the window
myApp.title("ttk styles for frames")

# Create a ttk Style instance
style = ttk.Style()

# Use the 'alt' theme for ttk widgets
style.theme_use('alt')

# Create a style for the main frame
style.configure('Main.TLabelframe', background='yellow', borderwidth=5)

# Create a main frame using ttk LabelFrame with the 'Main.TLabelframe' style
mainFrame = ttk.LabelFrame(myApp, text="MAIN FRAME", style='Main.TLabelframe')
mainFrame.grid(row=0, column=0, padx=10, pady=10)

# Label within the main frame without style
labelTitle = Label(mainFrame, text="Label without style", bg="beige", width=30, height=2, relief=GROOVE)
labelTitle.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ttk Label within the main frame with custom style applied
style.configure('Custom.TLabel', background='red', foreground='yellow', borderwidth=10,
                width=30, height=2, relief=GROOVE)
labelTitle1 = ttk.Label(mainFrame, text="Label with style", style='Custom.TLabel')
labelTitle1.grid(row=2, column=0, columnspan=4, padx=5, pady=10)

# Create another ttk LabelFrame with different configuration
subFrame = ttk.LabelFrame(myApp, text="SUB FRAME")
subFrame.grid(row=1, column=0, padx=10, pady=10)

# Label within the sub frame with custom style applied
labelTitle2 = ttk.Label(subFrame, text="Label in sub frame - ttk")
labelTitle2.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

# Configure custom style for ttk labels in sub frame
style.configure('Sub.TLabel', background='blue', foreground='white', borderwidth=5)

# Apply the custom style to the label within sub frame
labelTitle2.configure(style='Sub.TLabel')
# Adjust padding and alignment for all child widgets of the main myAppdow
for item in myApp.winfo_children():
    item.grid_configure(padx=10, pady=10, ipadx=5, ipady=5, sticky=NW)
# Start the tkinter event loop
myApp.mainloop()
