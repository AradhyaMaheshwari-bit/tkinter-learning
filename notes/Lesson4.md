# Lesson 4: Updating Widgets with `config()`

## Learning Objectives

By the end of this lesson you'll understand:

* What `config()` does.
* How to change a widget after it has been created.
* How a button can modify a label.
* Why we don't create a new label every time we want new text.

---

## The Problem

So far, we've created labels like this:

```python
label = tk.Label(root, text="Hello")
label.pack()
```

The label displays:

```
Hello
```

Now suppose we want it to display:

```
Welcome!
```

Should we create a **new** label?

```python
new_label = tk.Label(root, text="Welcome!")
new_label.pack()
```

No.

That would create another label below the first one.

Instead, we want to **change the existing label**.

---

# Meet `config()`

Every widget has a method called `config()`.

Think of it as:

> "Update the configuration (settings) of this widget."

For example:

```python
label.config(text="Welcome!")
```

Now the same label changes from:

```
Hello
```

to

```
Welcome!
```

No new label is created.

The existing label is simply updated.

---

# Your First Interactive GUI

```python
import tkinter as tk

root = tk.Tk()

root.title("Lesson 4")
root.geometry("400x250")


def change_text():
    label.config(text="Button Clicked!")


label = tk.Label(root, text="Hello")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

root.mainloop()
```

Run it.

Initially:

```
Hello
```

Click the button:

```
Button Clicked!
```

The text changes.

Notice:

Nothing new appears.

The existing label changes.

---

# Let's Understand It

Initially:

```python
label = tk.Label(root, text="Hello")
```

creates a label.

When you click the button:

```python
change_text()
```

runs.

Inside it:

```python
label.config(text="Button Clicked!")
```

changes one property of the existing label.

Think of it like changing a person's shirt.

It's still the same person.

Only one attribute has changed.

---

# Why Does `change_text()` Know About `label`?

You might notice something interesting.

The function is written **before** the label is created.

```python
def change_text():
    label.config(...)
```

Yet it still works.

Why?

Because Python doesn't execute the function body when you define it.

It only remembers:

> "When someone calls me, execute these statements."

Later:

```python
label = tk.Label(...)
```

creates the label.

Even later:

The button is clicked.

Only then does Python execute:

```python
label.config(...)
```

At that moment, `label` already exists.

---

# Experiment 1

Change:

```python
label.config(text="Button Clicked!")
```

to

```python
label.config(text="Welcome to Tkinter!")
```

What changes?

---

# Experiment 2

Click the button five times.

Questions:

* Does another label appear?
* Does anything different happen on the second click?

---

# Experiment 3

Create two buttons.

```python
def hello():
    label.config(text="Hello")


def goodbye():
    label.config(text="Goodbye")
```

Connect each function to its own button.

Predict before running:

* What happens if you click Hello?
* Then Goodbye?
* Then Hello again?

---

# What Else Can `config()` Change?

Not just text.

It can change almost every property.

For example:

```python
label.config(
    text="Success!",
    fg="white",
    bg="green"
)
```

or

```python
label.config(
    font=("Arial", 24)
)
```

You're modifying the same widget, not replacing it.

---

# Mental Model

Think of a widget as an object with properties.

Initially:

```
Label

text = "Hello"
fg   = black
bg   = default
font = Arial 12
```

When you call:

```python
label.config(text="Welcome")
```

Only this changes:

```
text = "Welcome"
```

Everything else stays the same.

---

# Challenge 1

Create a program with:

* One label displaying:

```
Waiting...
```

* Two buttons:

```
Start
Stop
```

Requirements:

* Clicking **Start** changes the label to:

```
Running
```

* Clicking **Stop** changes the label to:

```
Stopped
```

---

# Challenge 2

Answer these in your own words:

1. What is the purpose of `config()`?
2. Why don't we create a new label every time we want different text?
3. When `label.config(text="Hello")` runs, does it create a new widget or modify the existing one?
4. Why can `change_text()` use the variable `label` even though the function is defined before `label` is created?

---

## One Small Best Practice

Notice that our function directly accesses `label`:

```python
def change_text():
    label.config(text="Button Clicked!")
```

This is perfectly fine for small Tkinter programs and for learning.

Later, as your applications become larger, we'll learn cleaner ways to organize widgets and callbacks. For now, this approach is simple, readable, and exactly what you should use.

Complete the three experiments, the challenge program, and answer the four questions. Once you're comfortable with `config()`, you'll have enough knowledge to start building a functional GUI version of your calculator.
