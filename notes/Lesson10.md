# Lesson 10 – Frames

This is one of the most important design concepts in Tkinter.

Remember the rule:

> **Never mix `pack()` and `grid()` in the same parent.**

Soon you'll ask:

> "Then how do real applications use both?"

The answer is **Frames**.

A `Frame` is essentially a container widget that can hold other widgets.

For example:

```
Window
│
├── Frame (Header)
│     ├── Label
│     └── Entry
│
└── Frame (Buttons)
      ├── 7
      ├── 8
      ├── 9
      └── ...
```

Each `Frame` is its own parent.

That means you can safely do something like:

* Use `pack()` to arrange the frames inside the main window.
* Use `grid()` to arrange buttons inside the button frame.

This is a fundamental concept in Tkinter and a technique you'll use in almost every non-trivial GUI application.

---

Excellent. This lesson is one of the biggest steps toward writing professional Tkinter applications.

Until now, every widget has had the same parent:

```python
root
```

That works for small programs.

But imagine a calculator.

```
+--------------------------------+
|           Display              |
+--------------------------------+
| 7 | 8 | 9 | ÷ |
| 4 | 5 | 6 | × |
| 1 | 2 | 3 | - |
| 0 | . | = | + |
+--------------------------------+
```

Would you really want all of those widgets directly inside `root`?

Not really.

Instead, we group related widgets together.

That's exactly what **Frame** does.

---

## Learning Objectives

By the end of this lesson you'll understand:

* What a `Frame` is.
* Why `Frame`s are useful.
* Parent-child relationships.
* How `Frame`s solve the `pack()` vs `grid()` problem.
* How real applications are structured using frames.

---

# What is a Frame?

A `Frame` is simply a **container widget**.

It doesn't exist to display information.

Its purpose is to **hold other widgets**.

Think of a Frame as a box.

```
Window
│
├── Frame
│     ├── Label
│     ├── Button
│     └── Entry
│
└── Another Frame
      ├── Button
      ├── Button
      └── Button
```

---

# Think of a House

Imagine your window is a house.

```
House
```

Without rooms:

```
House

Table
Bed
Chair
TV
Kitchen
Sofa
```

Everything is in one place.

Now imagine the house has rooms.

```
House

Living Room
    TV
    Sofa

Bedroom
    Bed

Kitchen
    Table
```

A **Frame** is one of those rooms.

It helps organize widgets.

---

# Creating Your First Frame

```python
import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)

frame.pack()

root.mainloop()
```

Run it.

Question:

What do you see?

Answer:

Nothing.

---

# Why?

Exactly like a Label before calling `pack()`...

The Frame exists.

But unlike a Label...

A Frame has **no visible content**.

Its job isn't to display text.

It's just an empty container.

Think of an empty cardboard box.

Until you put something inside it, you barely notice it's there.

---

# Let's Put Something Inside

```python
import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)

frame.pack()

label = tk.Label(frame, text="Inside the Frame")

label.pack()

root.mainloop()
```

Notice something.

Earlier you wrote:

```python
tk.Label(root)
```

Now you're writing:

```python
tk.Label(frame)
```

The parent changed.

The Label now belongs to the Frame.

---

# Parent Hierarchy

```
root
│
└── Frame
      │
      └── Label
```

Instead of:

```
root
│
└── Label
```

---

# Why Is This Useful?

Imagine a calculator.

Instead of:

```
root

Entry
Button
Button
Button
Button
Button
Button
Button
Button
Button
Button
Button
Button
Button
Button
Button
Button
Button
```

You organize it.

```
root

Display Frame
    Entry

Button Frame
    7
    8
    9
    +

History Frame
    ...
```

Already much easier to understand.

---

# The `pack()` vs `grid()` Problem

Remember this?

```python
label.pack()

button.grid(...)
```

inside `root`

❌ Error.

But now look.

```python
root
│
├── Display Frame
└── Button Frame
```

We can do:

```python
display_frame.pack()

button_frame.pack()
```

because the Frames are children of `root`.

Then inside the Display Frame:

```python
entry.pack()
```

Inside the Button Frame:

```python
button.grid(...)
```

No problem.

Why?

Because they're **different parents**.

---

# Visualizing It

```
root
│
├── display_frame
│      │
│      └── Entry
│
└── button_frame
       │
       ├── Button
       ├── Button
       └── Button
```

Each parent chooses **one** layout manager.

Not the whole application.

Only that parent.

---

# Experiment 1

Run:

```python
import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)

frame.pack()

tk.Label(frame, text="A").pack()
tk.Label(frame, text="B").pack()

root.mainloop()
```

Questions:

* Where do the labels appear?
* Who is their parent?

---

# Experiment 2

Predict before running:

```python
import tkinter as tk

root = tk.Tk()

top = tk.Frame(root)
bottom = tk.Frame(root)

top.pack()

bottom.pack()

tk.Label(top, text="Top").pack()

tk.Label(bottom, text="Bottom").pack()

root.mainloop()
```

What do you think you'll see?

---

# Experiment 3

Run:

```python
import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, bg="lightblue")

frame.pack()

tk.Label(frame, text="Inside").pack()

root.mainloop()
```

Question:

Do you notice the blue background?

If not, why do you think that is?

*(Hint: think about how big the Frame actually is.)*

---

# Challenge 1

Create this hierarchy:

```
root

Header Frame
    Label : "Calculator"

Main Frame
    Entry

Button Frame
    Button : "1"
    Button : "2"
```

You don't need to worry about alignment yet.

Just create the hierarchy correctly.

---

# Challenge 2

Answer these in your own words:

1. What is a `Frame`?
2. Why do we use `Frame`s?
3. What is the parent of a widget inside a `Frame`?
4. How do `Frame`s allow us to use both `pack()` and `grid()` in one application?
5. Why doesn't an empty `Frame` appear to do anything?

---

## One Important Thought

Notice something beautiful about Tkinter.

You already know how to create widgets:

```python
tk.Label(...)
tk.Button(...)
tk.Entry(...)
```

Now you've learned:

```python
tk.Frame(...)
```

A `Frame` is just another widget.

The only difference is **what it's designed to contain**.

Labels display text.

Buttons trigger actions.

Entries store editable text.

Frames organize other widgets.

That's why Tkinter feels so consistent—almost every component follows the same creation and layout pattern.

Complete the experiments and challenges. Once you're comfortable with Frames, we'll move to **Tkinter Variables (`StringVar`, `IntVar`, etc.)**, which make keeping your interface synchronized with your program much cleaner.
