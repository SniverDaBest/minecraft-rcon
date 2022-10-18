from rcon import *
from tkinter import Tk
import tkinter as tk

window = Tk()
window.geometry("640x480")
window.title("Minecraft RCON")

textBox = tk.Text(window,height=1,width=20)
sendBtn = tk.Button(window,text="Send command")

window.mainloop()