# Lesson 1: Your First Tkinter Window

## Learning Objectives

By the end of this lesson, you'll know:

* What Tkinter is
* How to create a window
* What `Tk()` does
* What `mainloop()` does
* How the program executes

---

# What is Tkinter?

Tkinter is Python's standard library for creating **desktop GUI (Graphical User Interface)** applications.

Instead of this:

```text
Enter your choice:
```

you'll create windows with buttons, text boxes, menus, and more.

---

# Your First Program

Create `01_window.py`:

```python
import tkinter as tk

root = tk.Tk()

root.title("My First Tkinter App")

root.geometry("500x300")

root.mainloop()
```

Run it.

You should see a window titled **My First Tkinter App**.

---

# Let's Understand Every Line

## 1. Import

```python
import tkinter as tk
```

We import the Tkinter library.

We rename it to `tk` because we'll use it a lot.

This is the standard convention.

---

## 2. Create the application

```python
root = tk.Tk()
```

This is the most important line.

It creates the **main application window**.

Think of it like this:

```
Without Tk()
↓

Nothing exists.

With Tk()
↓

A window exists.
```

Everything you create later (buttons, labels, text boxes) will belong to this window.

---

## 3. Set the title

```python
root.title("My First Tkinter App")
```

Changes

```
tk
```

to

```
My First Tkinter App
```

---

## 4. Set the size

```python
root.geometry("500x300")
```

Means

```
500 pixels wide
300 pixels high
```

Format:

```python
"WIDTHxHEIGHT"
```

Notice:

It's the lowercase letter **x**, not the multiplication sign.

Examples:

```python
root.geometry("800x600")
```

```python
root.geometry("300x300")
```

---

## 5. Start the application

```python
root.mainloop()
```

This is the **heart** of every Tkinter program.

Without it:

* The window opens
* Immediately closes
* Program ends

With it:

* The window stays open
* Waits for user actions
* Responds to clicks
* Responds to typing

Think of it like this:

```
Create window

↓

Display window

↓

Wait...

↓

User clicks

↓

User types

↓

Keep waiting...

↓

User closes window

↓

Program ends
```

---

# Execution Flow

Your program executes like any normal Python program.

```
Start

↓

import tkinter

↓

Create window

↓

Set title

↓

Set size

↓

Enter mainloop()

↓

Wait for events

↓

Window closed

↓

Program ends
```

---

# Experiment Time

Don't just read—modify the code.

Try changing:

### Experiment 1

```python
root.title("Calculator")
```

---

### Experiment 2

```python
root.geometry("900x500")
```

---

### Experiment 3

```python
root.geometry("250x250")
```

Observe how the window changes.

---

### Experiment 4

Comment out:

```python
# root.mainloop()
```

Run the program.

Notice what happens.

This experiment will help you understand why `mainloop()` is essential.

---

# Challenge

Without looking back:

1. Create a window.
2. Set the title to **Tkinter Playground**.
3. Make it **700×400**.
4. Run it successfully.

If you can do that from memory, you've understood the core of Lesson 1.

---

## Before Lesson 2

Once you've completed the challenge, try answering these questions in your own words:

1. What does `tk.Tk()` create?
2. Why do we write `import tkinter as tk`?
3. What does `geometry("500x300")` mean?
4. What is the purpose of `mainloop()`?
5. What happens if `mainloop()` is removed?

Don't worry about getting the wording perfect. Explaining these concepts yourself is one of the best ways to make them stick.
