# Lesson 5: Layout Managers

## Learning Objectives

By the end of this lesson, you'll understand:

* What a layout manager is.
* Why `pack()` exists.
* How `pack()` decides where widgets go.
* What `side`, `fill`, `expand`, `padx`, and `pady` do.
* Why `grid()` exists (we'll learn it next).

---

# What is a Layout Manager?

Creating a widget only creates the object.

```python
label = tk.Label(root, text="Hello")
```

Displaying it:

```python
label.pack()
```

But `pack()` is doing **two jobs**:

1. Making the widget visible.
2. Deciding **where** to put it.

That second job is called **layout management**.

A **layout manager** is simply a system that decides where widgets should be placed inside their parent.

---

# Think of an Empty Room

Imagine your root window is an empty room.

```
+-----------------------------+
|                             |
|                             |
|                             |
|                             |
+-----------------------------+
```

Now you bring in a chair.

```
chair.pack()
```

Tkinter says:

> "I'll find a place for it."

Bring another chair.

```
chair2.pack()
```

Tkinter says:

> "I'll put it below the first one."

You never specified coordinates.

The layout manager decided.

---

# Default `pack()`

Example:

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="One").pack()
tk.Label(root, text="Two").pack()
tk.Label(root, text="Three").pack()

root.mainloop()
```

Result:

```
One
Two
Three
```

This is exactly what you've already observed.

By default:

* Widgets are stacked vertically.
* The order depends on the order of `pack()` calls.

---

# `side`

Now let's tell `pack()` to behave differently.

```python
tk.Label(root, text="One").pack(side="left")
```

Now the label sticks to the **left side**.

Available values:

```python
side="top"
side="bottom"
side="left"
side="right"
```

Example:

```python
tk.Label(root, text="A").pack(side="left")
tk.Label(root, text="B").pack(side="left")
tk.Label(root, text="C").pack(side="left")
```

Result:

```
A  B  C
```

Notice that they're now arranged horizontally.

---

# Experiment 1

Run:

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="A").pack(side="left")
tk.Label(root, text="B").pack(side="left")
tk.Label(root, text="C").pack(side="left")

root.mainloop()
```

Observe:

* Where does A appear?
* Where does B appear?
* Why isn't C under B?

---

# `padx` and `pady`

Look at this:

```
ABC
```

Everything is touching.

Let's add spacing.

```python
tk.Label(root, text="A").pack(side="left", padx=10)
```

Now:

```
A     B     C
```

`padx`

→ Horizontal spacing.

`pady`

→ Vertical spacing.

---

# Experiment 2

Run:

```python
tk.Label(root, text="A").pack(pady=20)
tk.Label(root, text="B").pack(pady=20)
tk.Label(root, text="C").pack(pady=20)
```

Question:

* What changed?

---

# `fill`

Imagine a label:

```
Hello
```

Normally, the label is only as wide as its text.

What if you want it to stretch?

```python
label.pack(fill="x")
```

Now the widget stretches across the available width.

Possible values:

```python
fill="x"
fill="y"
fill="both"
```

Think of it as:

> "Grow to fill the available space."

---

# `expand`

This one confuses many beginners.

Suppose your window is very large.

Without `expand`:

```
Hello

(empty space)
```

With

```python
expand=True
```

Tkinter says:

> "If there's extra room in the parent, give some of it to this widget."

The widget gets allocated extra space.

It doesn't necessarily become bigger by itself unless it also uses `fill`.

A useful mental model:

* `expand` → **Who gets the extra space?**
* `fill` → **What should the widget do with the space it receives?**

We'll experiment with this more once we start using `Frame` widgets.

---

# Important Rule

There are **three** layout managers:

```python
pack()
grid()
place()
```

Inside the **same parent**, don't mix `pack()` and `grid()`.

For example:

```python
label.pack()
button.grid(row=0, column=0)
```

inside the same `root`

❌ This causes a runtime error.

Tkinter expects one layout manager per parent.

Later you'll learn how `Frame`s let you use different layout managers in different parts of a window.

---

# Challenge 1

Predict the output before running:

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="1").pack(side="left")
tk.Label(root, text="2").pack(side="right")
tk.Label(root, text="3").pack(side="left")

root.mainloop()
```

Questions:

* Where will `1` appear?
* Where will `2` appear?
* Where will `3` appear?

---

# Challenge 2

Answer these in your own words:

1. What is a layout manager?
2. Besides displaying the widget, what other job does `pack()` perform?
3. What does `side="left"` change?
4. What is the difference between `padx` and `pady`?
5. Without using the internet, explain the difference between `fill` and `expand` based on today's lesson. It's okay if you're not completely sure—that's what learning is for.

---

## A Small Preview

You've probably noticed something already.

Even with `side="left"`, creating a calculator would be awkward.

```
7 8 9 + 4 5 6 - 1 2 3 =
```

That's because `pack()` isn't designed for grid-like interfaces.

In the next lesson, you'll learn `grid()`, which places widgets using **rows and columns**—exactly what a calculator keypad needs. That's why almost every Tkinter calculator you see uses `grid()` for the buttons.
