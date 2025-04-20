#import both tk and ttk
import tkinter as tk
from tkinter import ttk
'''
Create an instance of 'Style', similar to myApp = tk.Tk()
Use this instance to define and configure styles for ttk widgets

'''
style = ttk.Style()
# check what the current theme is use is:
print()
print("current style theme in use: ", style.theme_use())
print()
# prints: current style theme in use:  aqua

#  check what other themes are available:
print("style themes: ",style.theme_names())
print()
# prints: style themes:  ('aqua', 'clam', 'alt', 'default', 'classic')
#change style
style.theme_use('alt')
print("new style theme in use: ", style.theme_use())
print()
# prints:new style theme in use:  alt

