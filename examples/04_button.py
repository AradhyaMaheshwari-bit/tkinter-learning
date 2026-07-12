import tkinter as tk

root = tk.Tk()

root.title("Lesson 3")
root.geometry("400x250")


def add():
    print("Add")

def sub():
    print("Subtract")

def multiply():
    print("Multiply")

button1 = tk.Button(root, text="Add", command=add)
button2 = tk.Button(root, text="Subtract", command=sub)
button3 = tk.Button(root, text="Multiply", command=multiply)

button1.pack()       # button1.pack(pady=20) pady: paddint(empty space) This creates vertical empty space above and below the widget
button2.pack()
button3.pack()

root.mainloop()
