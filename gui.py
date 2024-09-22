from tkinter import *
from tkinter import filedialog
from ctypes import windll
import serial
from PIL import Image, ImageTk
import time 
import asyncio
import threading

try:
    arduino = serial.Serial(port='COM5',  baudrate=115200, timeout=.1)
except:
    print("Failed to connect to Arduino! (Are you connected to the right port?)")
    exit()
windll.shcore.SetProcessDpiAwareness(1)

# Globals, constants and stuff
activeSend = False
async def sendData(cmd):
    print("Trying to send data to Arduino...")
    arduino.write(bytes(cmd, 'utf-8'))
    data = arduino.readline().decode('utf-8').strip()
    while (data == ""):
        data = arduino.readline().decode('utf-8').strip()
    print("received response: " + str(data))
def show_frame(frame):
    frame.tkraise()


def stringToBraille(string):
    # Start from upper left corner
    # Down, Down, Down, Right, Up, Up
    # End at upper right corner 
    braille = {
        'a': "100000",
        'b': "110000",
        'c': "100001",
        'd': "100011",
        'e': "100010",
        'f': "110001",
        'g': "110011",
        'h': "110010",
        'i': "010001",
        'j': "010011",
        'k': "101000",
        'l': "111000",
        'm': "101001",
        'n': "101011",
        'o': "101010",
        'p': "111001",
        'q': "111011",
        'r': "111010",
        's': "011001",
        't': "011011",
        'u': "101100",
        'v': "111100",
        'w': "011110",
        'x': "101101",
        'y': "101111",
        'z': "101110",
        ' ': "000000",
        '#': "001111",
        '1': "100000",
        '2': "110000",
        '3': "100001",
        '4': "100011",
        '5': "100010",
        '6': "110001",
        '7': "110011",
        '8': "110010",
        '9': "010001",
        '0': "010011",
        ',': "010000",
        '.': "010110",
        ';': "011000",
        ':': "010010",
        '?': "011100",
        '!': "011010",
    }   
    output = ""
    for char in string:
        char = char.lower()
        braille_char = braille.get(char)
        if (braille_char != None):
            output+=str(braille_char)
    return output[::-1]

async def readFile():
    global activeSend
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()
            lines = file_content.split("\n")
            if (activeSend == True):
                print("Already sending data to Arduino! Please wait for the current data to finish sending.")
                return
            activeSend = True
            for line in lines:
                print(stringToBraille(line))
                await sendData(stringToBraille(line))
            activeSend = False

def start_async_read_file():
    asyncio.run(readFile())

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
Button(root, text="clockwise", command=lambda: sendData("clockwise")).pack()
Button(root, text="counterclockwise",command=lambda: sendData("counterclockwise")).pack()

# File selector
Button(root, text="Open Text File", command=lambda: threading.Thread(target=start_async_read_file).start()).pack()
root.mainloop()

