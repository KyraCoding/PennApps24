from tkinter import *
from ctypes import windll
import pyglet, os

pyglet.font.add_file('static/RobotoMono-Regular.ttf')
windll.shcore.SetProcessDpiAwareness(1)

ws = Tk()

ws.title("PennApps 2024 Project")
Tk.geometry(ws, "1440x900")
message = Label(ws, font=('RobotoMono-Regular',25), text="PennApps24")
message.pack()

ws.mainloop()