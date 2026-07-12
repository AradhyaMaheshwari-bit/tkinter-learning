import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.geometry("900x500")

# tk.Label(root, text="One").pack(pady=10)                # Default side="top"
# tk.Label(root, text="Two").pack(pady=10)                # pady = vertical spacing (up and down of widget)
# tk.Label(root, text="Three").pack(pady=10)
tk.Label(root, text="One").pack(side="left")
tk.Label(root, text="A").pack(side="top")
# tk.Label(root, text="B").pack(side="bottom")
# tk.Label(root, text="C").pack(side="right")
# tk.Label(root, text="A").pack(side="left", padx=10)     # padx = horizontal spacing (left and right of widget)
# tk.Label(root, text="B").pack(side="left", padx=10)
# tk.Label(root, text="C").pack(side="left", padx=10)

# label = tk.Label(
#     root,
#     text="Python GUI",
#     font=("Arial", 24),     # ("font_family", font_size)
#     fg="dark green",              # 'f'ore'g'round_color or text_color # default="black"
#     bg="dark green",             # 'b'ack'g'round_color # default="white" or "lightgrey"
# ).pack(fill="x")

# label = tk.Label(
#     root,
#     text="Python GUI",
#     font=("Arial", 24),     # ("font_family", font_size)
#     fg="dark green",              # 'f'ore'g'round_color or text_color # default="black"
#     bg="dark green",             # 'b'ack'g'round_color # default="white" or "lightgrey"
# ).pack(fill="y")



label = tk.Label(
    root,
    text="Python GUI",
    font=("Arial", 24),     # ("font_family", font_size)
    fg="dark green",              # 'f'ore'g'round_color or text_color # default="black"
    bg="dark green",             # 'b'ack'g'round_color # default="white" or "lightgrey"
).pack(fill="both",expand=True)

root.mainloop()
