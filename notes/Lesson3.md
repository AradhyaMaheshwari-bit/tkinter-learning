# Lesson 3: Buttons and Events

## Learning Objectives

By the end of this lesson, you'll understand:

* What a `Button` widget is.
* How to create a button.
* What the `command` parameter does.
* Why we pass a function instead of calling it.
* How button clicks fit into Tkinter's event loop.

---

# What is a Button?

A button is a widget that waits for the user to click it.

When clicked, it performs an action.

Examples:

* Calculator → `+`, `-`, `=`
* Browser → Refresh
* YouTube → Play
* Login page → Login

All of these are buttons waiting for a click.

---

# Your First Button

```python
import tkinter as tk

root = tk.Tk()

root.title("Lesson 3")
root.geometry("400x250")

def say_hello():
    print("Hello!")

button = tk.Button(root, text="Click Me", command=say_hello)

button.pack(pady=20)

root.mainloop()
```

Run it.

What happens?

Nothing happens when the window opens.

When you click the button:

```
Hello!
```

is printed in the terminal.

Notice that the output appears in the **terminal**, not inside the window.

---

# Understanding Every New Line

## 1. Creating a Function

```python
def say_hello():
    print("Hello!")
```

Nothing new here.

It's just a normal Python function.

---

## 2. Creating a Button

```python
button = tk.Button(root, text="Click Me", command=say_hello)
```

Break it down:

* `root` → parent widget
* `text` → text displayed on the button
* `command` → function to execute when the button is clicked

---

# The Most Important Line

```python
command=say_hello
```

Notice something:

There are **no parentheses**.

Not:

```python
command=say_hello()
```

This is one of the biggest beginner mistakes.

---

## Why No Parentheses?

Let's compare.

### Case 1 (Correct)

```python
command=say_hello
```

You're giving Tkinter the **function itself**.

Think of it as saying:

> "Here's the function. Call it later when the button is clicked."

Nothing is executed yet.

---

### Case 2 (Incorrect)

```python
command=say_hello()
```

Python immediately executes:

```python
say_hello()
```

before the window even appears.

So:

1. `"Hello!"` prints immediately.
2. The function finishes.
3. `None` (the function's return value) is assigned to `command`.
4. Clicking the button does nothing.

---

# Think of It Like This

Imagine I ask:

> "Give me your phone number."

You write it on paper.

I can call you later.

That's:

```python
command=say_hello
```

Now imagine instead I say:

> "Call yourself right now."

That's:

```python
say_hello()
```

The action happens immediately.

Nothing is left for later.

---

# How the Event Loop Uses `command`

Remember our mental model?

```python
while application_is_running:

    event = wait_for_event()

    if event == button_clicked:
        run_button_function()
```

Now imagine you created:

```python
command=say_hello
```

Tkinter stores a reference to that function.

When the click event occurs:

```
User clicks button
        │
        ▼
Tkinter detects click
        │
        ▼
Looks at command
        │
        ▼
Calls say_hello()
```

That's why nothing happens until you click.

---

# Experiment 1

Change:

```python
print("Hello!")
```

to

```python
print("Welcome to Tkinter")
```

Does anything else need to change?

---

# Experiment 2

Create two buttons.

```python
def hello():
    print("Hello")

def goodbye():
    print("Goodbye")

button1 = tk.Button(root, text="Hello", command=hello)
button2 = tk.Button(root, text="Goodbye", command=goodbye)

button1.pack()
button2.pack()
```

Observe:

* Which function runs when each button is clicked?
* Does clicking one affect the other?

---

# Experiment 3

What do you think this will do?

```python
def hello():
    print("Hello")

button = tk.Button(root, text="Click", command=hello())

button.pack()
```

**Don't run it yet.**

Predict:

1. When will `"Hello"` print?
2. What will happen when you click the button?

Then run it and compare your prediction.

---

# Challenge 1

Create a window with three buttons:

* Add
* Subtract
* Multiply

For now, each button should simply print its own name in the terminal when clicked.

For example:

Click **Add**:

```
Add
```

Click **Subtract**:

```
Subtract
```

---

# Challenge 2

Without looking back, answer these questions:

1. What is the purpose of the `command` parameter?
2. Why do we write:

```python
command=my_function
```

instead of

```python
command=my_function()
```

3. When is the function actually executed?

---

## A Small Preview

In the next lesson, you'll connect a **Button** with a **Label**.

Instead of printing to the terminal, you'll make a button **change the text on the window itself**.

That's the moment your GUI starts feeling like a real application.
