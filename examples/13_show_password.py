import tkinter as tk

root = tk.Tk()
root.title("Login Page")
root.geometry("500x300")

tk.Label(root, text="+" + "-" * 80 + "+").pack()

login = tk.Frame(root)
login.pack()

tk.Label(login, text="Username:").grid(row=0, column=0, padx=10)
username_text = tk.StringVar()
tk.Entry(login, textvariable=username_text).grid(row=0, column=1)

tk.Label(login, text="Password:").grid(row=2, column=0, padx=10)
password_text = tk.StringVar()
password_entry = tk.Entry(login, textvariable=password_text)
password_entry.grid(row=2, column=1)

password_entry.config(show="*")
password_hidden = True

def show_password():
    global password_hidden
    if password_hidden:
        password_entry.config(show="")
        show_password_button.config(text="🙈 Hide")
    else:
        password_entry.config(show="*")
        show_password_button.config(text="👁 Show")
    password_hidden = not password_hidden

show_password_button = tk.Button(login, text="👁 Show", command=show_password)
show_password_button.grid(row=2, column=2)

tk.Label(root, text="+" + "-" * 80 + "+").pack()

root.mainloop()
