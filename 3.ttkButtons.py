# Import necessary modules from tkinter
from tkinter import *
from tkinter import ttk

# Create a tkinter myAppdow instance
myApp = Tk()

# Set the dimensions of the myAppdow
myApp.geometry("400x100")

# Set the background color of the myAppdow
myApp.configure(background="LightBlue2")

# Allow the myAppdow to be resizable
myApp.resizable("true", "true")

# Set the title of the myAppdow
myApp.title("ttk styles for buttons")

# Create a ttk Style instance
style = ttk.Style()

# Print available style themes
print("style themes: ", style.theme_names())

# Print the current style theme in use
print("current style theme in use: ", style.theme_use())

# Change the style theme in use to 'alt'
style.theme_use('alt')

# Print the current style theme in use after changing
print("current style theme in use: ", style.theme_use())

# Configure the style for all TButton widgets
style.configure('TButton', background='black', foreground='white', width=12, borderwidth=5, focusthickness=5, focuscolor='yellow')

# Map the style for active state of TButton widgets to change background color to red
style.map('TButton', background=[('active', 'red')])

# Create a ttk Button widget with text "Click Me!" and command 'tapCount'
buttonTap = ttk.Button(myApp, text="Click Me!", command='tapCount')

# Place the ttk Button widget in the myAppdow
buttonTap.grid(row=7, column=0, padx=50, pady=50)

# Create a ttk Button widget with text "Quit" and command to close the myAppdow
buttonQuit = ttk.Button(myApp, text="Quit", command=myApp.destroy)

# Place the ttk Button widget in the myAppdow
buttonQuit.grid(row=7, column=2, padx=50, pady=50)

# Start the tkinter event loop
myApp.mainloop()
