import tkinter as tk

root = tk.Tk()
root.title("Lesson 13: Challenge 1")

label = tk.Label(root, text="Waiting...")
label.pack()

def key(event):
    label.config(text=f"You pressed:\n{event.keysym}")

root.bind("<Key>", key)

root.mainloop()
