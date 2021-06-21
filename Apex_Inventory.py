from pyHook import HookManager
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

from PIL import ImageTk, Image
import os
import pyautogui

counter = 0

def on_keyboard_event(event):
    global counter
    counter += 1
    if event.Key == 'Tab' and event.WindowName == 'Apex Legends' and counter == 1:
        takeScreenshot()
    else:
        counter = 0
    root.update()
    return True

def takeScreenshot():
    screenshot = pyautogui.screenshot(region=(705,750,1160,550))
    screenshot.save("inventory.png")
    img = ImageTk.PhotoImage(Image.open("inventory.png"))
    label = Label(root, image = img)
    label.image = img
    label.place(x=0, y=5)

hm = HookManager()
hm.KeyUp = on_keyboard_event
hm.HookKeyboard()
root = tkinter.Tk(className='\Apex Inventory')
label = tkinter.Label(root)
root.geometry("1165x560")
root.resizable(width=False, height=False)
frame = Frame(root, width=1160, height=560)

label.pack()
root.mainloop()