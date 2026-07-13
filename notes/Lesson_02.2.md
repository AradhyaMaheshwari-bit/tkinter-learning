# Lesson 2.1 — Styling Labels

Now that you can create labels, let's make them look better.

Create a new file or modify your existing one:

```python
import tkinter as tk

root = tk.Tk()
root.title("Label Styling")
root.geometry("500x300")

label = tk.Label(
    root,
    text="Hello Tkinter!",
    font=("Arial", 20),
    fg="blue",
    bg="yellow"
)

label.pack()

root.mainloop()
```

Run it and observe:

* The text is larger.
* The text is blue.
* The background behind the label is yellow.

### Let's break down the new arguments

#### `font`

```python
font=("Arial", 20)
```

This is a tuple.

* `"Arial"` → font family
* `20` → font size (points)

Try changing:

```python
font=("Times New Roman", 30)
```

or

```python
font=("Courier New", 18)
```

and see the difference.

---

#### `fg`

```python
fg="blue"
```

`fg` stands for **foreground**, which means the **text color**.

Examples:

```python
fg="red"
fg="green"
fg="purple"
fg="black"
```

---

#### `bg`

```python
bg="yellow"
```

`bg` stands for **background**, which is the color behind the label.

Try:

```python
bg="lightblue"
```

or

```python
bg="black"
```

If you choose a dark background, remember to choose a light `fg` so the text stays readable.

---

### Mini Challenge

Create a label that says:

```
Python GUI
```

with:

* Font: Arial
* Size: 24
* Text color: white
* Background color: dark green

After you've done that, tell me:

1. What happens if you remove `bg`?
2. What happens if you remove `fg`?
3. What do you think will happen if you set both `fg` and `bg` to the same color? (Predict first, then test.)

---
