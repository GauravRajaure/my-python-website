import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# Style for buttons
def configure_style():
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('TButton', background='lightBlue2', foreground='white', width=12, borderwidth=1, focusthickness=1, focuscolor='blue')
    style.map('TButton', background=[('active', 'red')])
    style.configure('big.TButton', font=(None, 14), foreground="blue4")

# function to handle button to show image:
def showImg(): 
    # configure_style()
# image details
    default = "img/default.png"
    image = Image.open(default)
    image = image.resize((100, 100), Image.Resampling.LANCZOS)
    imgDefault = ImageTk.PhotoImage(image)
# Set up button to show image
    imgButton = ttk.Button(myImgApp,image = imgDefault, style="TButton")
    imgButton.grid(row=4, column=0, sticky=tk.NE)
    imgButton.image = imgDefault

#  Initial set up
myImgApp = tk.Tk() # Create a basic window - myImgApp
myImgApp.title("Lecture Image Demo") # Give a name to the myImgAppdow
myImgApp.geometry("300x300") # set the myImgAppdow size
myImgApp.configure(background = "LightBlue2")

showImgButton = ttk.Button(myImgApp, text = "Show Image", command = showImg)
showImgButton.grid(row = 2, column = 0, sticky = tk.E)
QuitButton = ttk.Button(myImgApp, text = "Quit", command = myImgApp.destroy)
QuitButton.grid(row = 2, column = 1, sticky = tk.E)
configure_style()
myImgApp.mainloop() # keeps the myImgAppdow alive,
 # listenimng for any events until closed
