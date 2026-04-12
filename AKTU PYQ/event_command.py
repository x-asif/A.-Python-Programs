import tkinter as tk

def greet():
    print("Hello! Button clicked")

root = tk.Tk()

btn = tk.Button(root, text="Click Me", command=greet)
btn.pack()

root.mainloop()