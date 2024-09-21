from tkinter import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

ws = Tk()

ws.title("PennApps 2024 Project")
Tk.geometry(ws, "1440x900")
message = Label(ws,  text="PennApps24")
message.pack()

ws.mainloop()