import tkinter as tk

root = tk.Tk()

root.title("Lesson 4")
root.geometry("400x250")

def start():
    label.config(text="Running")

def stop():
    label.config(text="Stopped")

label = tk.Label(root, text="Waiting...")
label.pack(pady=20)

b1 = tk.Button(root, text="Start", command=start)
b1.pack()
b2 = tk.Button(root, text="Stop", command=stop)
b2.pack()

root.mainloop()
