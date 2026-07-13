# Lesson 11: Tkinter Variables (`StringVar`, `IntVar`, etc.)

## Learning Objectives

By the end of this lesson, you'll understand:

* What Tkinter Variables are.
* Why they exist.
* What `StringVar` is.
* `set()`
* `get()`
* How widgets automatically update.
* Why `StringVar` is cleaner than repeatedly using `config()` or `Entry.insert()`.

---

# The Problem

Let's think about the calculator.

Suppose your display is an `Entry`.

When the user presses:

```text
7
```

we want the Entry to show:

```text
7
```

One way is:

```python
entry.delete(0, tk.END)
entry.insert(0, "7")
```

Now the user presses:

```text
8
```

Again:

```python
entry.delete(0, tk.END)
entry.insert(0, "78")
```

Then:

```text
9
```

Again:

```python
entry.delete(0, tk.END)
entry.insert(0, "789")
```

It works...

but it's repetitive.

Tkinter gives us something better.

---

# Meet `StringVar`

Instead of thinking:

> The Entry stores the text.

Think:

> The Entry displays whatever is inside a variable.

That variable is called a **Tkinter Variable**.

---

# Think of It Like This

Without `StringVar`

```text
Entry

contains

Hello
```

With `StringVar`

```text
StringVar
     │
     ▼
Entry
```

The Entry becomes a **viewer**.

The variable stores the data.

---

# Creating One

```python
text = tk.StringVar()
```

That's it.

You've created a Tkinter variable that stores strings.

---

# Setting a Value

```python
text.set("Hello")
```

Now the variable contains:

```text
Hello
```

---

# Getting the Value

```python
print(text.get())
```

Output:

```text
Hello
```

Notice something.

This looks exactly like:

```python
entry.get()
```

The API is intentionally similar.

---

# Connecting It to an Entry

Here's the magic.

```python
import tkinter as tk

root = tk.Tk()

text = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=text
)

entry.pack()

text.set("Hello")

root.mainloop()
```

Run it.

Question:

Who put

```text
Hello
```

inside the Entry?

You never called:

```python
entry.insert()
```

---

# The Answer

This line:

```python
textvariable=text
```

creates a connection.

```text
StringVar
     │
     ▼
Entry
```

Whenever the variable changes...

The Entry updates automatically.

---

# Even Cooler

```python
text.set("Python")
```

↓

Entry immediately becomes

```text
Python
```

No:

```python
entry.delete()

entry.insert()
```

No:

```python
entry.config()
```

Tkinter does it automatically.

---

# The Other Direction

Suppose the user types:

```text
Tkinter
```

Guess what happens?

```python
print(text.get())
```

Output:

```text
Tkinter
```

The synchronization works both ways.

```text
User

↓

Entry

↓

StringVar
```

and

```text
Program

↓

StringVar

↓

Entry
```

---

# Why Is This Better?

Without `StringVar`

```python
entry.delete(0, tk.END)
entry.insert(0, "100")
```

With `StringVar`

```python
text.set("100")
```

Much cleaner.

---

# Experiment 1

Run:

```python
import tkinter as tk

root = tk.Tk()

text = tk.StringVar()

entry = tk.Entry(root, textvariable=text)

entry.pack()

text.set("Python")

root.mainloop()
```

Questions:

* Does the Entry show `"Python"`?
* Did you ever call `insert()`?

---

# Experiment 2

Run:

```python
text.set("Hello")

print(text.get())
```

Predict the output.

---

# Experiment 3

Run:

```python
text.set("Python")

text.set("Tkinter")
```

Predict:

What appears in the Entry?

Both?

Only one?

Why?

---

# Other Tkinter Variables

Tkinter has several variable types.

```python
tk.StringVar()

tk.IntVar()

tk.DoubleVar()

tk.BooleanVar()
```

Examples:

```python
age = tk.IntVar()

price = tk.DoubleVar()

is_logged_in = tk.BooleanVar()
```

For the calculator...

We'll mainly use:

```python
StringVar
```

---

# Challenge 1

Create:

* One Entry
* One Button

When the button is clicked:

```python
text.set("Button Clicked")
```

Observe what happens.

---

# Challenge 2

Answer these in your own words.

### 1.

Why do Tkinter Variables exist?

---

### 2.

What is the relationship between

```python
StringVar
```

and

```python
Entry
```

---

### 3.

What is the purpose of

```python
textvariable=text
```

---

### 4.

Which is cleaner?

```python
entry.delete(0, tk.END)
entry.insert(0, "100")
```

or

```python
text.set("100")
```

Why?

---

# One Important Clarification

Don't confuse:

```python
text = "Hello"
```

with

```python
text = tk.StringVar()
```

The first is a **normal Python string variable**.

The second is a **Tkinter object** specifically designed to stay synchronized with widgets.

---

## A Question Before You Start

I want you to think about this.

Suppose you write:

```python
text = tk.StringVar()

text.set("Hello")
```

but your `Entry` is:

```python
entry = tk.Entry(root)
```

Notice that **`textvariable=text` is missing.**

**Prediction:**

1. What will the Entry display?
2. What will `print(text.get())` output?

Don't run it immediately. Try to reason it out using the mental model we've built throughout the Tkinter lessons.
