import tkinter as tk

root = tk.Tk()
root.title("Lesson12")
root.geometry("400x200")

text = tk.StringVar()
# text.set("Hello")

def print_text():
    print(text.set("Button Clicked"))

entry = tk.Entry(root, textvariable=text)
entry.pack()
entry.focus()

# tk.Label(root, textvariable=text).pack()

tk.Button(root, text="Click", command=print_text).pack()

# text.set("Python")




root.mainloop()
