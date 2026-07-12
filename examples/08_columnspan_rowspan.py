import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.geometry("300x500")

display = tk.Label(
    root,
    text="12345",
    bg="lightgray"
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="ew"
)

tk.Button(root, text="=").grid(
    row=3,
    column=2,
    columnspan=2
)

tk.Button(root, text="+").grid(
    row=0,
    column=3,
    rowspan=4
)

root.mainloop()
