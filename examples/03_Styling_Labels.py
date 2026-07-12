import tkinter as tk

root = tk.Tk()
root.title("Label Styling")
root.geometry("500x300")

label = tk.Label(
    root,
    # text="Hello Tkinter!",
    text="Python GUI",
    font=("Arial", 24),     # ("font_family", font_size)
    fg="dark green",              # 'f'ore'g'round_color or text_color # default="black"
    bg="dark green",              # 'b'ack'g'round_color # default="white" or "lightgrey"
)

label.pack()

root.mainloop()
