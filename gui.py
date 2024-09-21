from tkinter import *
from ctypes import windll
import serial
import time 

arduino = serial.Serial(port='COM5',  baudrate=115200, timeout=.1)

windll.shcore.SetProcessDpiAwareness(1)


def sendCommand(cmd):
    print("sending command: " + cmd)
    arduino.write(bytes(cmd, 'utf-8'))

ws = Tk()
ws.title("PennApps 2024 Project")
Tk.geometry(ws, "720x450")
message = Label(ws, text="PennApps24")
message.pack()
Button(ws, text="clockwise", command=lambda: sendCommand("clockwise")).pack()
Button(ws, text="counterclockwise",command=lambda: sendCommand("counterclockwise")).pack()

ws.mainloop()

