import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.geometry("900x500")

# tk.Label(root, text="A").grid(row=0, column=0)
# tk.Label(root, text="B").grid(row=0, column=1)
# tk.Label(root, text="C").grid(row=0, column=2)
# tk.Label(root, text="1").grid(row=1, column=0)
# tk.Label(root, text="2").grid(row=1, column=1)
# tk.Label(root, text="3").grid(row=1, column=2)

# tk.Label(root, text="A").grid(
#     row=0,
#     column=0,
#     padx=10,
#     pady=10
# )

tk.Label(root, text="A").grid(row=0, column=0)
tk.Label(root, text="B").grid(row=0, column=1)
tk.Label(root, text="C").grid(row=0, column=2)
tk.Label(root, text="D").grid(row=1, column=0)
tk.Label(root, text="E").grid(row=1, column=1)
tk.Label(root, text="F").grid(row=1, column=2)
tk.Label(root, text="G").grid(row=2, column=0)
tk.Label(root, text="H").grid(row=2, column=1)
tk.Label(root, text="I").grid(row=2, column=2)

root.mainloop()
