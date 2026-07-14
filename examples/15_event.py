import tkinter as tk

root = tk.Tk()

def pressed(event):
    print(f"{event.keysym} Key Pressed")

# root.bind("event", function_name)
root.bind("<Key>", pressed)

def clicked(event):
    print(event.x)
    print(event.y)

root.bind(
    "<Double-Button-1>",
    clicked
)

root.mainloop()

'''
Keyboard:
    <Key>
    <Return>
    <Escape>
    <BackSpace>

Mouse:
    <Button-1>
    <Button-2>
    <Button-3>
    <Double-Button-1>
'''



