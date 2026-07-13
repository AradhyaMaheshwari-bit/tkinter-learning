# Lesson 9: Entry Widget

Up until now, your GUI has only been able to **display** information.

```
Label
 ↓
Shows text
```

But what if we want the user to **type** something?

For example:

```
Username: [____________]

Password: [____________]
```

or

```
Calculator

+-------------------+
| 12345             |
+-------------------+
```

A `Label` can't do that.

We need another widget.

---

# Learning Objectives

By the end of this lesson you'll understand:

* What an `Entry` widget is.
* How to create one.
* How to read user input.
* How to insert text.
* How to delete text.
* Why calculators use an `Entry` instead of a `Label`.

---

# What is an Entry Widget?

An **Entry** widget is a widget that allows the user to enter and edit **a single line of text**.

Examples:

```
Username
+----------------------+
| Aradhya             |
+----------------------+
```

```
Search
+----------------------+
| Tkinter             |
+----------------------+
```

```
Calculator
+----------------------+
| 12345               |
+----------------------+
```

Unlike a `Label`, the user can interact with it.

---

# Your First Entry

```python
import tkinter as tk

root = tk.Tk()

root.title("Lesson 9")
root.geometry("400x200")

entry = tk.Entry(root)

entry.pack(pady=20)

root.mainloop()
```

Run it.

Questions:

* What appears?
* Can you click inside it?
* Can you type?
* What happens if you press Backspace?

---

# Understanding the Code

```python
entry = tk.Entry(root)
```

Exactly like `Label` and `Button`.

You're creating another widget.

Its parent is:

```python
root
```

Then:

```python
entry.pack()
```

displays it.

Nothing new so far.

---

# The Important Difference

A `Label`

```
Shows text.
```

An `Entry`

```
Stores text.
Allows editing.
Allows typing.
```

---

# Reading User Input

Suppose the user types:

```
Python
```

How does our program know that?

The `Entry` object has a method:

```python
get()
```

Think of it as asking:

> "Entry, what text do you currently contain?"

---

Example:

```python
import tkinter as tk

root = tk.Tk()

def show_text():
    print(entry.get())

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root,
                   text="Print",
                   command=show_text)

button.pack()

root.mainloop()
```

Run it.

Type:

```
Hello
```

Click **Print**.

Terminal:

```
Hello
```

---

# What does `get()` return?

Suppose the Entry contains

```
12345
```

Then

```python
entry.get()
```

returns

```python
"12345"
```

Notice the quotes.

It always returns a **string**.

Even if you type

```
100
```

the return value is

```python
"100"
```

not

```python
100
```

This is important for calculators because eventually we'll convert those strings into numbers.

---

# Inserting Text

We don't always wait for the user.

Sometimes **our program** wants to put text inside the Entry.

Method:

```python
insert()
```

Example:

```python
entry.insert(0, "Hello")
```

Result:

```
+----------------------+
| Hello               |
+----------------------+
```

---

## Why the `0`?

Syntax:

```python
insert(index, text)
```

The first argument tells Tkinter:

> "Where should I insert this text?"

Remember:

Python counts from 0.

```
Hello

01234
```

So

```python
entry.insert(0, "Python ")
```

produces

```
Python Hello
```

because it inserts before the first character.

If you used

```python
entry.insert(5, "!")
```

you'd get

```
Hello!
```

---

# Deleting Text

Method:

```python
delete()
```

Example:

```python
entry.delete(0, tk.END)
```

This removes everything.

Think of it as:

```
Delete

from index 0

to the end.
```

---

# Why `tk.END`?

Suppose the Entry contains:

```
Python GUI
```

Instead of counting characters,

Tkinter provides

```python
tk.END
```

meaning

> "Go to the last character."

So

```python
entry.delete(0, tk.END)
```

means:

> Delete everything.

---

# A Typical Pattern

Very common in Tkinter:

```python
def clear():

    entry.delete(0, tk.END)
```

or

```python
def reset():

    entry.delete(0, tk.END)

    entry.insert(0, "0")
```

You'll use this in the calculator.

---

# Experiment 1

Run:

```python
entry.insert(0, "Python")
```

Questions:

* Can you still edit the text?
* Is the inserted text different from user-typed text?

---

# Experiment 2

Run:

```python
entry.insert(0, "Hello")
entry.insert(0, "Python ")
```

Predict first.

What do you think the Entry will display?

Then run it.

---

# Experiment 3

Run:

```python
entry.insert(0, "Python GUI")

entry.delete(0, 6)
```

Predict first.

What remains?

---

# Challenge 1

Create a small program.

Window contains:

* One Entry
* One Button labeled:

```
Show
```

When the button is clicked,

print whatever the user typed into the terminal.

---

# Challenge 2

Answer these in your own words:

1. What is the difference between a `Label` and an `Entry`?
2. Why does `entry.get()` always return a string?
3. What is the purpose of `insert()`?
4. Why do we write

```python
entry.delete(0, tk.END)
```

instead of

```python
entry.delete(0, 100)
```

---

## One Thought Before You Start

Notice how similar this feels to previous widgets:

```python
label = tk.Label(...)
button = tk.Button(...)
entry = tk.Entry(...)
```

Tkinter is very consistent.

Once you learn one widget, the next ones feel familiar because they all follow the same pattern:

1. Create the widget.
2. Place it with a layout manager.
3. Configure or interact with it using methods.

That's one of the reasons Tkinter is an excellent library for learning GUI programming.

Complete the three experiments, the challenge program, and answer the four questions. Once you're comfortable with `Entry`, we'll move on to **Frames**, which will let you organize your calculator into clean, reusable sections.

---

# One More Important Method

Before we finish `Entry`, there's one method I want to introduce because you'll use it constantly in the calculator.

## `focus()`

Suppose your window opens.

The cursor isn't always inside the Entry.

Sometimes you have to click first.

Instead:

```python
entry.focus()
```

When the window opens:

```
+---------------------+
| |                   |
+---------------------+
```

The cursor is already there.

The Entry has keyboard focus.

Think of it as saying:

> "This widget should receive keyboard input immediately."

You'll almost certainly use this in your calculator so the user can start typing without an extra click.

---

# Lesson 9 Summary

You now know how to:

* ✅ Create an `Entry`
* ✅ Read text using `get()`
* ✅ Insert text using `insert()`
* ✅ Delete text using `delete()`
* ✅ Set keyboard focus using `focus()`

These five methods cover most of what you'll need for a calculator display.

---

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
