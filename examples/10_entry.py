import tkinter as tk

root = tk.Tk()

root.title("Lesson 9")
root.geometry("400x200")

# def show_text():
#     print(entry.get())

# entry = tk.Entry(root)
# entry.pack(pady=20)

# entry.insert(0, "Hello")      # insert(index, text)
# # entry.insert(0, "Python ")
# entry.insert(5, "!")

# entry.delete(0, tk.END)       # delete(start, end-1(unless it is tk.END))

# entry.insert(0, "Python GUI")
# entry.delete(0, 6)

# def reset():
#     entry.delete(0, tk.END)
#     entry.insert(0, "0")

# button = tk.Button(root, text="Print", command=show_text)
# button.pack()


def print_entry():
    print(entry.get())

entry = tk.Entry(root)
entry.pack(pady=20)
entry.focus()            # this method makes sure that our cursor is already present on the widget rather than us haveing to click first.

button = tk.Button(root, text="Show", command=print_entry)
button.pack(pady=20)

root.mainloop()
