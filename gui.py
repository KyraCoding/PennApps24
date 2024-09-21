from tkinter import *
from tkinter import filedialog
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

def show_frame(frame):
    frame.tkraise()

def stringToBraille(string):
    # Start from upper left corner
    # Down, Down, Down, Right, Up, Up
    # End at upper right corner 
    braille = {
        'a': [True, False, False, False, False, False],
        'b': [True, True, False, False, False, False],
        'c': [True, False, False, False, False, True],
        'd': [True, False, False, False, True, True],
        'e': [True, False, False, False, True, False],
        'f': [True, True, False, False, False, True],
        'g': [True, True, False, False, True, True],
        'h': [True, True, False, False, True, False],
        'i': [False, True, False, False, False, True],
        'j': [False, True, False, False, True, True],
        'k': [True, False, True, False, False, False],
        'l': [True, True, True, False, False, False],
        'm': [True, False, True, False, False, True],
        'n': [True, False, True, False, True, True],
        'o': [True, False, True, False, True, False],
        'p': [True, True, True, False, False, True],
        'q': [True, True, True, False, True, True],
        'r': [True, True, True, False, True, False],
        's': [False, True, True, False, False, True],
        't': [False, True, True, False, True, True],
        'u': [True, False, True, True, False, False],
        'v': [True, True, True, True, False, False],
        'w': [False, True, True, True, True, False],
        'x': [True, False, True, True, False, True],
        'y': [True, False, True, True, True, True],
        'z': [True, False, True, True, True, False],
        ' ': [False, False, False, False, False, False],
        '#': [False, False, True, True, True, True],
        '1': [True, False, False, False, False, False],
        '2': [True, True, False, False, False, False],
        '3': [True, False, False, False, False, True],
        '4': [True, False, False, False, True, True],
        '5': [True, False, False, False, True, False],
        '6': [True, True, False, False, False, True],
        '7': [True, True, False, False, True, True],
        '8': [True, True, False, False, True, False],
        '9': [False, True, False, False, False, True],
        '0': [False, True, False, False, True, True]
    }   
    output = []
    for char in string:
        char = char.lower()
        braille_char = braille.get(char)
        if (braille_char != None):
            output.append(braille_char)
    return output

def readFile():
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()
            lines = file_content.split("\n")
            for line in lines:
                print(stringToBraille(line))

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

# File selector
Button(root, text="Open Text File", command=readFile).pack()
root.mainloop()

