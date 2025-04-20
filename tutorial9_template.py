import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def save_images(path, image_dict):
    VALID_IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff")
    pass


def show_black_button(buttons, frames, color_img_dict):
    pass


def show_blue_button(frames, color_img_dict):
    pass


def show_red_button(frames, color_img_dict):
    pass


def clear_all(buttons, frames):
    # Reset button states

    pass

    # Clear widgets from frames and reset background color
    pass


def config_styles():
    pass


def create_frames(myApp):
    pass


def create_buttons(app, frames, color_img_dict):
    pass


def main():
    myColorApp = tk.Tk()
    myColorApp.title("Color App demo Lambda function")
    myColorApp.configure(background="teal")
    myColorApp.geometry("800x500")
    # images folder location
    imgPath = "img/"

    myColorApp.mainloop()


main()
