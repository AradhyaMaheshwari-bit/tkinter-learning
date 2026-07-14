##  This is the final lesson.

And it's fitting because **everything you've learned so far has been event-driven**—you just didn't know the name for it.

When you wrote:

```python
tk.Button(
    root,
    text="Login",
    command=check_login
)
```

You were already responding to an event.

The event was:

> **Button Clicked**

Now we're going to respond to many more events.

---

# Lesson 13: Events (`bind()`)

## Learning Objectives

By the end of this lesson you'll understand:

* What an event is.
* What `bind()` does.
* The `event` object.
* Keyboard events.
* Mouse events.
* Why `command=` and `bind()` both exist.
* When to use each.

---

# What is an Event?

An event is simply:

> **Something the user does.**

Examples:

```text
User clicks a button.

↓

Event
```

```text
User presses Enter.

↓

Event
```

```text
User presses A.

↓

Event
```

```text
User moves the mouse.

↓

Event
```

```text
User closes the window.

↓

Event
```

Everything is an event.

---

# Wait...

Haven't we already been using events?

Yes.

```python
command=show_password
```

means:

> When the button click event happens,
> call this function.

That's event-driven programming.

---

# Then why do we need `bind()`?

Because `command` only works for **buttons**.

Suppose you want:

```text
Press Enter

↓

Login
```

There isn't a button click.

There is a **keyboard event**.

That's where `bind()` comes in.

---

# Your First Event

```python
import tkinter as tk

root = tk.Tk()

def pressed(event):
    print("Key Pressed")

root.bind("<Key>", pressed)

root.mainloop()
```

Run it.

Click the window first.

Now press random keys.

Question:

How many times is the function called?

---

# Understanding `bind()`

```python
root.bind(
    "<Key>",
    pressed
)
```

Read it as English.

> Root,

when a

```text
<Key>
```

event happens,

call

```python
pressed
```

---

# Notice Something

Earlier:

```python
command=show_password
```

Function:

```python
def show_password():
```

No parameters.

Now:

```python
root.bind(...)
```

Function:

```python
def pressed(event):
```

There's a parameter.

Why?

---

# The Event Object

When Tkinter calls your function...

it tells you **what happened**.

That information is stored in

```python
event
```

Think of it as a little package.

```text
User presses A

↓

Tkinter

↓

event
```

Inside that package is information.

---

# Which Key Was Pressed?

Example:

```python
def pressed(event):

    print(event.keysym)
```

Now press

```text
A
```

Output:

```text
a
```

Press

```text
Enter
```

Output:

```text
Return
```

Press

```text
Escape
```

Output:

```text
Escape
```

Press

```text
Left Arrow
```

Output:

```text
Left
```

Very useful.

---

# Logging In With Enter

Suppose we already have

```python
def login():
```

This won't work.

Why?

Because `bind()` always passes an event.

Instead write:

```python
def login(event):
```

or

```python
def login(event=None):
```

Now the same function can be used for:

```python
command=login
```

and

```python
bind(...)
```

We'll talk about that in a moment.

---

# Enter Key

```python
root.bind(
    "<Return>",
    login
)
```

Now pressing Enter calls

```python
login()
```

Well...

actually

```python
login(event)
```

because Tkinter passes the event object.

---

# Mouse Events

Suppose we want to detect a mouse click anywhere.

```python
root.bind(
    "<Button-1>",
    clicked
)
```

Button 1 means:

Left Mouse Button.

---

Function:

```python
def clicked(event):

    print(event.x)

    print(event.y)
```

Now click.

Output:

```text
145

82
```

Those are the mouse coordinates.

---

# Other Common Events

Keyboard:

```text
<Key>

<Return>

<Escape>

<BackSpace>
```

Mouse:

```text
<Button-1>

<Button-2>

<Button-3>

<Double-Button-1>
```

Don't memorize all of them.

The common ones are enough.

---

# command vs bind

Very important.

Suppose you have

```python
Button
```

Should you use

```python
command=
```

or

```python
bind()
```

Usually

```python
command=
```

Why?

Because it's simpler.

Use `bind()` when you need:

* Keyboard shortcuts
* Mouse coordinates
* Key presses
* Events other than button clicks

---

# Experiment 1

Run:

```python
import tkinter as tk

root = tk.Tk()

def key(event):

    print(event.keysym)

root.bind("<Key>", key)

root.mainloop()
```

Questions:

* What happens when you press A?
* Enter?
* Escape?
* Arrow keys?

Observe.

---

# Experiment 2

Run:

```python
def mouse(event):

    print(event.x, event.y)

root.bind(
    "<Button-1>",
    mouse
)
```

Question:

What do the numbers represent?

---

# Experiment 3

Modify your login window.

Instead of only

```python
Login Button
```

also allow:

```text
Press Enter

↓

Login
```

No extra button.

Just bind the Enter key.

---

# Challenge 1

Create a program.

Window contains one Label.

Initially:

```text
Waiting...
```

Whenever a key is pressed:

Change the Label to:

```text
You pressed:

A
```

or

```text
You pressed:

Enter
```

using

```python
event.keysym
```

Hint:

You've already learned

```python
label.config()
```

---

# Challenge 2

Answer these.

### 1.

What is an event?

---

### 2.

Why does a bound function receive

```python
event
```

as a parameter?

---

### 3.

When should we use

```python
command=
```

instead of

```python
bind()
```

---

### 4.

What information does

```python
event.keysym
```

provide?

---

### 5.

Why won't this work?

```python
root.bind(
    "<Return>",
    login
)

def login():
```

---

# 🧩 Final Mini Exercise Before the Calculator

Take your login application and make these improvements:

### Requirements

* Pressing **Enter** should trigger Login.
* Pressing **Escape** should close the window.
* If login succeeds:

  * Show the success message box.
  * Clear both Entry widgets.
* If login fails:

  * Show the error message box.
  * Clear only the password field.
  * Put the cursor back into the password Entry using `focus()`.

This exercise combines almost everything you've learned in the Tkinter module:

* Windows
* Labels
* Buttons
* Entry
* StringVar
* Frames
* `pack()`
* `grid()`
* `config()`
* Boolean state
* Message boxes
* Events
* `focus()`

---
