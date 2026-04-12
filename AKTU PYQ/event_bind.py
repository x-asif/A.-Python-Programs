import tkinter as tk

def on_click(event):
    print("Mouse clicked at:", event.x, event.y)

root = tk.Tk()

label = tk.Label(root, text="Click anywhere here", bg="lightblue")
label.pack(padx=20, pady=20)

# Bind left mouse click
label.bind("<Button-1>", on_click)

root.mainloop()