import tkinter as tk

root = tk.Tk()
root.title("Lesson 10")
root.geometry("400x200")

# frame = tk.Frame(root)
# frame.pack()

# label = tk.Label(frame, text="Inside the Frame")
# label.pack()

# tk.Label(frame, text="A").pack()
# tk.Label(frame, text="B").pack()

# root.mainloop()





# top = tk.Frame(root)
# bottom = tk.Frame(root)

# top.pack()

# bottom.pack()

# tk.Label(top, text="Top").pack()

# tk.Label(bottom, text="Bottom").pack()

# root.mainloop()




# frame = tk.Frame(root, bg="lightblue")

# frame.pack()

# tk.Label(frame, text="Inside").pack(fill="x")

# root.mainloop()



header = tk.Frame(root)
header.pack()

main = tk.Frame(root)
main.pack()

button = tk.Frame(root)
button.pack()

tk.Label(header, text="Calculator").pack()
tk.Entry(main).pack()
tk.Button(button, text="1").grid(row=0, column=0,padx=10)
tk.Button(button, text="2").grid(row=0, column=1, padx=10)

root.mainloop()
