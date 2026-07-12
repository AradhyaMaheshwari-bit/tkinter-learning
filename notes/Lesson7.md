# Lesson 7 – `columnspan` and `rowspan`

Remember this calculator?

```text
+-----------------------+
|         12345         |
+-----+-----+-----+-----+
|  7  |  8  |  9  |  ÷  |
+-----+-----+-----+-----+
|  4  |  5  |  6  |  ×  |
+-----+-----+-----+-----+
|  1  |  2  |  3  |  -  |
+-----+-----+-----+-----+
|  0  |  .  |  =  |  +  |
+-----+-----+-----+-----+
```

Notice the display at the top.

It isn't just in one cell.

It stretches across all four columns.

How do we tell Tkinter:

> "This widget should occupy **more than one cell**."

That's exactly what `columnspan` does.

---

## Your First Example

```python
import tkinter as tk

root = tk.Tk()

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
```

Don't worry about `sticky` yet—we'll cover it next.

Focus only on:

```python
columnspan=4
```

This tells Tkinter:

> "Start at column 0 and occupy **4 columns**."

Conceptually, it looks like:

```text
+----+----+----+----+
|      Display       |
+----+----+----+----+
```

instead of:

```text
+----+----+----+----+
|Disp|    |    |    |
+----+----+----+----+
```

---

## Another Example

```python
tk.Button(root, text="=").grid(
    row=3,
    column=2,
    columnspan=2
)
```

This button occupies:

```text
+----+----+----------+
| 0  | .  |    =     |
+----+----+----------+
```

---

## `rowspan`

`rowspan` works the same way, but vertically.

```python
tk.Button(root, text="+").grid(
    row=0,
    column=3,
    rowspan=4
)
```

Conceptually:

```text
+----+----+----+----+
| 7  | 8  | 9  |    |
+----+----+----+ +  |
| 4  | 5  | 6  |    |
+----+----+----+    |
| 1  | 2  | 3  |    |
+----+----+----+    |
| 0  | .  | =  |    |
+----+----+----+----+
```

The `+` button spans four rows.

---

# Experiments

### Experiment 1

Predict before running:

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="A", bg="yellow").grid(
    row=0,
    column=0,
    columnspan=3
)

root.mainloop()
```

What do you expect `columnspan=3` to do?

---

### Experiment 2

Predict:

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Tall", bg="lightblue").grid(
    row=0,
    column=0,
    rowspan=2
)

tk.Label(root, text="X").grid(row=0, column=1)
tk.Label(root, text="Y").grid(row=1, column=1)

root.mainloop()
```

How do you think the layout will look?

---

## Questions

1. Why is `columnspan` useful for a calculator?
2. What's the difference between `columnspan=4` and creating four separate labels?
3. If a widget starts at `column=1` and has `columnspan=3`, which columns does it occupy?

Once you understand spans, we'll move on to `sticky`, which controls how a widget is aligned **inside** its grid cell. That's the last major layout concept you'll need before we start assembling the calculator GUI.
