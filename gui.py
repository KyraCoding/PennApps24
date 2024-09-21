from tkinter import *
from ctypes import windll
import serial
from PIL import Image, ImageTk
import time 

try:
    arduino = serial.Serial(port='COM5',  baudrate=115200, timeout=.1)
except:
    print("Failed to connect to Arduino!")

windll.shcore.SetProcessDpiAwareness(1)

# Globals, constants and stuff
def sendCommand(cmd):
    print("sending command: " + cmd)
    arduino.write(bytes(cmd, 'utf-8'))
    
root = Tk()


# Background
image = Image.open("assets/background.png")
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Window config
root.title("PennApps 2024 Project")
Tk.geometry(root, "1440x900")
root.resizable(width=False, height=False)

# Title text
message = Label(root, text="PennApps24")
message.pack()
Button(root, text="clockwise", command=lambda: sendCommand("clockwise")).pack()
Button(root, text="counterclockwise",command=lambda: sendCommand("counterclockwise")).pack()

root.mainloop()

