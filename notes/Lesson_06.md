# Lesson 6: `grid()` – The Layout Manager for Tables

## Learning Objectives

By the end of this lesson, you'll understand:

* Why `grid()` exists.
* How rows and columns work.
* How to place widgets using `row` and `column`.
* The difference between `pack()` and `grid()`.
* Why calculators almost always use `grid()`.

---

# Why Do We Need `grid()`?

Imagine building a calculator using only `pack()`.

```
7
8
9
+
4
5
6
-
1
2
3
=
```

You could eventually make it work using nested `Frame`s, but it's unnecessarily complicated.

A calculator is naturally a **table**.

```
+---+---+---+---+
| 7 | 8 | 9 | ÷ |
+---+---+---+---+
| 4 | 5 | 6 | × |
+---+---+---+---+
| 1 | 2 | 3 | - |
+---+---+---+---+
| 0 | . | = | + |
+---+---+---+---+
```

That's exactly what `grid()` is designed for.

---

# Think of an Excel Sheet

Imagine the window is divided into invisible cells.

```
        Column
         0   1   2
       +---+---+---+
Row 0  |   |   |   |
       +---+---+---+
Row 1  |   |   |   |
       +---+---+---+
Row 2  |   |   |   |
       +---+---+---+
```

Every widget occupies one (or more) cells.

---

# Your First `grid()`

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="A").grid(row=0, column=0)

root.mainloop()
```

Question:

Where does **A** appear?

Answer:

Top-left corner.

Because:

* Row = 0 (first row)
* Column = 0 (first column)

Remember:

**Python starts counting from 0.**

---

# Adding More Labels

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="A").grid(row=0, column=0)
tk.Label(root, text="B").grid(row=0, column=1)
tk.Label(root, text="C").grid(row=0, column=2)

root.mainloop()
```

Result:

```
A   B   C
```

Notice how much simpler this is than using `pack(side="left")`.

---

# Adding Another Row

```python
tk.Label(root, text="1").grid(row=1, column=0)
tk.Label(root, text="2").grid(row=1, column=1)
tk.Label(root, text="3").grid(row=1, column=2)
```

Result:

```
A  B  C
1  2  3
```

You're literally filling cells in a table.

---

# Visualizing the Coordinates

```
       Column
        0    1    2
      +----+----+----+
Row 0 | A  | B  | C  |
      +----+----+----+
Row 1 | 1  | 2  | 3  |
      +----+----+----+
```

Every widget simply says:

> "I belong at `(row, column)`."

---

# Experiment 1

Predict before running:

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="X").grid(row=2, column=1)

root.mainloop()
```

Questions:

* Will it create rows 0 and 1 automatically?
* Where will **X** appear?

---

# Experiment 2

Run:

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="A").grid(row=0, column=0)
tk.Label(root, text="B").grid(row=2, column=2)

root.mainloop()
```

Observe:

* What happened to row 1?
* What happened to column 1?

---

# `padx` and `pady` with `grid()`

Just like with `pack()`:

```python
tk.Label(root, text="A").grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)
```

Padding still means spacing around the widget.

The concept doesn't change.

Only the layout manager changes.

---

# One Important Rule

You already know this, but now it makes more sense.

Inside the same parent:

```python
label.pack()
button.grid(...)
```

❌ Don't do this.

Because `pack()` and `grid()` are trying to control the same parent widget.

Tkinter doesn't know which layout manager should be in charge.

---

# Challenge 1

Without looking back, create this layout:

```
A  B  C
D  E  F
G  H  I
```

using only `grid()`.

---

# Challenge 2

Answer these in your own words:

1. Why is `grid()` better than `pack()` for a calculator?
2. What does `row=2, column=1` mean?
3. What happens if no widget is placed in `row=1`?
4. Can you skip row numbers or column numbers?
5. Why can't `pack()` and `grid()` both manage widgets inside the same parent?

---

## A Small Preview

Once you're comfortable with placing widgets in rows and columns, we'll learn how to make them **occupy multiple cells** using `columnspan` and `rowspan`.

For example, in a calculator, the display might span all four columns:

```
+-----------------------+
|         12345         |
+-----+-----+-----+-----+
|  7  |  8  |  9  |  ÷  |
+-----+-----+-----+-----+
```

That display isn't just one cell—it stretches across the entire top row. That's where `columnspan` comes in, and it's one of the most useful features of `grid()`.

---
