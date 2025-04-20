import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

myImgApp = tk.Tk() # Create a basic window - myImgApp
myImgApp.title("Lecture 9 Image Demo") # Give a name to the myImgAppdow
myImgApp.geometry("300x300") # set the myImgAppdow size
myImgApp.configure(background = "LightBlue2")

# function to handle button to show image:
def showImg():  
# image details
    default = "img/default.png"
    image = Image.open(default)
    image = image.resize((100, 100), Image.Resampling.LANCZOS)
    imgDefault = ImageTk.PhotoImage(image)

    print("image: "+str(imgDefault))
    # Set up label to show image
    imgLabel = tk.Label(myImgApp,image = imgDefault)
    imgLabel.grid(row=4, column=0, sticky=tk.NE)

    imgLabel.image = imgDefault

showImgButton = ttk.Button(myImgApp, text = "Show Image", command = showImg)
showImgButton.grid(row = 2, column = 0, sticky = tk.E)
QuitButton = ttk.Button(myImgApp, text = "Quit", command = myImgApp.destroy)
QuitButton.grid(row = 2, column = 1, sticky = tk.E)

myImgApp.mainloop() # keeps the myImgAppdow alive,
 # listenimng for any events until closed
