import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# messagebox.method_name("window_name", "message")
# messagebox.showinfo("Title", "Hello World")
# messagebox.showinfo("Information","Login Successful")

# def greet():
#     messagebox.showinfo("Greeting","Welcome to Tkinter!")

# messagebox.showwarning("Warning", "Battery Low")

# messagebox.showerror("Error","Invalid Password")

# answer = messagebox.askyesno("Exit", "Are you sure?")

# answer = messagebox.askyesno("Question", "Continue?")

# print(answer)

# print("Finished")

# messagebox.askokcancel()

# messagebox.askretrycancel()

# messagebox.askquestion()

# tk.Button(root,text="Click Me",command=greet).pack(pady=20)


def showinfo():
    messagebox.showinfo("Lesson12", "Experiment 3")
def showwarning():
    messagebox.showwarning("Security","Not Authorized")
def showerror():
    messagebox.showerror("Error", "Invalid option")
tk.Button(root,text="Click Me",command=showinfo).pack(pady=20)
tk.Button(root,text="Click Me",command=showwarning).pack(pady=20)
tk.Button(root,text="Click Me",command=showerror).pack(pady=20)

root.mainloop()
