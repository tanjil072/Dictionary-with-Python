import tkinter as tk
from tkinter import *

# creating Tk window
from tkinter import messagebox

master = Tk()
root = tk.Tk()

# setting geometry of tk window
master.geometry("500x400")

# button widget
b1 = Button(master, text="Search", width=10)
b1.place(relx=1, x=-120, y=20, anchor=NE)

# Entry widget
E1 = Entry(bd=3)
E1.place(relx=1, x=-420, y=22, height=30, width=190)

# label widget
l = Label(master, text="I'm a Label")
l.place(x=75, y=100)



mainloop()
