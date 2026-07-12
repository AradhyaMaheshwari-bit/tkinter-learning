# Lesson 2: Labels

## Learning Objectives

By the end of this lesson you'll understand:

* What a widget is
* What a Label is
* How to create one
* How to display it
* How widgets belong to the root window
* The difference between **creating** and **placing** a widget

---

# First, what is a Widget?

Everything you see in a GUI is called a **widget**.

Examples:

```text
Window
│
├── Label
├── Button
├── Entry
├── Checkbox
├── Radio Button
├── Menu
├── Frame
└── ...
```

Think of widgets as LEGO blocks.

You combine many widgets to build an application.

---

# What is a Label?

A Label simply **displays information**.

Examples:

```text
Simple Calculator
```

```text
Username
```

```text
Result: 25
```

Unlike an Entry widget, a Label **doesn't let the user type**.

It only shows information.

---

# Our First Label

Start with your previous code.

```python
import tkinter as tk

root = tk.Tk()

root.title("Lesson 2")
root.geometry("500x300")

label = tk.Label(root, text="Hello Tkinter!")

label.pack()

root.mainloop()
```

Run it.

You should see:

```text
+-----------------------------+
|                             |
|       Hello Tkinter!        |
|                             |
+-----------------------------+
```

---

# Let's understand every new line

## Creating a Label

```python
label = tk.Label(root, text="Hello Tkinter!")
```

Break it apart.

### `tk.Label`

Create a Label widget.

---

### `root`

This is the **parent**.

You're saying:

> Put this Label inside the root window.

Later you'll create Labels inside Frames.

Everything has a parent.

Think of it like a family tree.

```
root
│
├── Label
├── Button
└── Entry
```

---

### `text=`

The text that appears.

```python
text="Hello Tkinter!"
```

---

# Why doesn't this work?

Suppose you write only:

```python
label = tk.Label(root, text="Hello")
```

Run it.

You'll see...

Nothing.

Why?

Because you've only **created** the widget.

You haven't told Tkinter **where to put it**.

---

# Enter `pack()`

```python
label.pack()
```

This tells Tkinter:

> Display this widget in the window.

Think of it like moving furniture into a room.

Buying a chair isn't enough.

You have to place it inside the room.

---

# Create vs Display

Very important distinction.

Creating:

```python
label = tk.Label(...)
```

↓

Widget exists in memory.

---

Displaying:

```python
label.pack()
```

↓

Widget becomes visible.

---

# Experiment 1

Change the text.

```python
text="Simple Calculator"
```

Run it.

---

# Experiment 2

Create another Label.

```python
title = tk.Label(root, text="Simple Calculator")
title.pack()

author = tk.Label(root, text="Made by Aradhya")
author.pack()
```

What happens?

Observe carefully.

---

# Experiment 3

Create three Labels.

```python
A
B
C
```

using

```python
pack()
```

Notice how Tkinter automatically arranges them.

Don't worry **how** it decides yet.

We'll study layout managers in Lesson 5.

---

# Important Concept

Each Label is an **object**.

Just like:

```python
student = Student()
```

creates a Student object,

```python
label = tk.Label(...)
```

creates a Label object.

Later you'll call methods on it like

```python
label.config(...)
```

or

```python
label.destroy()
```

---

# Challenge 1

Create a window that displays:

```text
Python Tkinter
Learning GUI Development
Lesson 2
```

using **three Labels**.

---

# Challenge 2

Without looking at the notes, answer these:

1. What is a widget?
2. What is a Label used for?
3. Why do we pass `root` into `Label()`?
4. Why doesn't a Label appear until `pack()` is called?
5. What is the difference between creating a Label and displaying a Label?

---

## One thing I want you to notice

You've already encountered **two objects** in Tkinter:

```python
root = tk.Tk()

label = tk.Label(...)
```

Both are Python objects created from classes. Tkinter is heavily object-oriented, so as we progress you'll see more widgets created the same way. Understanding that these are objects—not special syntax—will make the rest of Tkinter much easier to learn.

Complete the two experiments and the two challenges, then we'll move on to styling Labels (fonts, colors, and alignment) before introducing buttons.
