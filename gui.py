import tkinter as tk

root = tk.Tk()
e = tk.Entry(root)
e.insert(0, "some text")

def some_callback(event): # note that you must include the event as an arg, even if you don't use it.
    e.delete(0, "end")
    return None

e.bind("<Button-1>", some_callback)

e.pack()