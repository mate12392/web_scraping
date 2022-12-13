import tkinter as tk
import os
from datetime import datetime

def Tkinter():
    global l
    m = tk.Tk()
    m.title("Package Manager")
    m.configure(width=800, height=500, background='AntiqueWhite2')
    """w = tk.Canvas(m, width=800, height=500, background='AntiqueWhite2')
    w.pack()
    w.create_line(30, 10, 30, 400)"""
    l = tk.Label(m, text=datetime.now())
    l.pack()
    b2 = tk.Button(m, text="Reload", command=reload, activeforeground='Red')
    b2.pack()
    m.mainloop()

def reload():
    global l
    l.configure(text=datetime.now())

Tkinter()