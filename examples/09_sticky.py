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

root.mainloop()
