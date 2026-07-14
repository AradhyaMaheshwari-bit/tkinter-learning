# Lesson 12: Message Boxes

## Learning Objectives

By the end of this lesson you'll understand:

* What a message box is.
* Different types of message boxes.
* Information dialogs.
* Warning dialogs.
* Error dialogs.
* Confirmation dialogs.
* How to use the user's response.

---

# What is a Message Box?

A message box is a **small popup window** used to communicate with the user.

You've seen them many times.

Examples:

```text
+--------------------------+
|         Information      |
|--------------------------|
| File saved successfully. |
|                          |
|          [ OK ]          |
+--------------------------+
```

or

```text
+----------------------------+
|          Error             |
|----------------------------|
| Division by zero.          |
|                            |
|          [ OK ]            |
+----------------------------+
```

or

```text
+------------------------------+
| Confirm Exit                 |
|------------------------------|
| Are you sure?                |
|                              |
|     [ Yes ]   [ No ]         |
+------------------------------+
```

---

# Importing Message Boxes

Message boxes are in a separate module.

```python
from tkinter import messagebox
```

Notice this isn't

```python
import tkinter as tk
```

It's another import from the Tkinter package.

Most programs use both.

```python
import tkinter as tk
from tkinter import messagebox
```

---

# Information Box

The simplest one.

```python
messagebox.showinfo(
    "Title",
    "Hello World!"
)
```

Run it.

Question:

What happens after clicking the button?

Observe carefully.

---

# What are these arguments?

```python
messagebox.showinfo(
    "Information",
    "Login Successful"
)
```

First argument:

```text
Information
```

↓

Window title.

Second argument:

```text
Login Successful
```

↓

Message shown inside.

---

# Using It With a Button

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def greet():
    messagebox.showinfo(
        "Greeting",
        "Welcome to Tkinter!"
    )

tk.Button(
    root,
    text="Click Me",
    command=greet
).pack(pady=20)

root.mainloop()
```

Click the button.

Notice:

The popup appears.

You can't interact with the main window until you close it.

We'll discuss why in a moment.

---

# Warning Box

Sometimes the program wants to warn the user.

```python
messagebox.showwarning(
    "Warning",
    "Battery Low"
)
```

Observe:

Different icon.

---

# Error Box

```python
messagebox.showerror(
    "Error",
    "Invalid Password"
)
```

Different icon again.

---

# Think About It

The code hardly changed.

Only this word changed.

```python
showinfo()

showwarning()

showerror()
```

That's one thing I like about Tkinter.

Its API stays consistent.

---

# Confirmation Dialog

This is where things become interesting.

```python
answer = messagebox.askyesno(
    "Exit",
    "Are you sure?"
)
```

Now something is returned.

Question:

What do you think `answer` contains?

Predict before running.

---

# The Return Value

Suppose the user clicks:

```text
Yes
```

Then

```python
answer
```

contains

```python
True
```

If the user clicks

```text
No
```

Then

```python
answer
```

contains

```python
False
```

This should remind you of something.

A boolean.

Exactly.

---

# Example

```python
def exit_program():

    answer = messagebox.askyesno(
        "Exit",
        "Are you sure?"
    )

    print(answer)
```

Click Yes.

Terminal:

```text
True
```

Click No.

Terminal:

```text
False
```

---

# Making Decisions

Now we can write

```python
answer = messagebox.askyesno(
    "Exit",
    "Exit application?"
)

if answer:

    print("Closing...")

else:

    print("Cancelled")
```

Exactly like any other boolean.

---

# Other Useful Dialogs

Tkinter also provides

```python
messagebox.askokcancel()

messagebox.askretrycancel()

messagebox.askquestion()
```

You don't need to memorize all of them.

The important idea is:

Some dialogs only display information.

Others return a value.

---

# When Should We Use Them?

Good examples:

✅ Invalid password

```python
showerror()
```

---

File saved

```python
showinfo()
```

---

Delete file?

```python
askyesno()
```

---

Low battery

```python
showwarning()
```

---

# Experiment 1

Run:

```python
messagebox.showinfo(
    "Hello",
    "Welcome!"
)

print("Finished")
```

Question:

When is

```text
Finished
```

printed?

Before closing the popup?

Or after?

Think first.

---

# Experiment 2

Run:

```python
answer = messagebox.askyesno(
    "Question",
    "Continue?"
)

print(answer)
```

Click

* Yes
* No

Observe.

---

# Experiment 3

Create three buttons.

One opens

```python
showinfo()
```

One opens

```python
showwarning()
```

One opens

```python
showerror()
```

Compare the icons.

---

# Challenge 1

Build a tiny login simulation.

Window:

```
Username Entry

Password Entry

Login Button
```

Logic:

If username is

```text
admin
```

and password is

```text
1234
```

Show

```python
showinfo()
```

Otherwise

```python
showerror()
```

Don't worry about security.

This is only practice.

---

# Challenge 2

Answer these.

### 1.

Why do we import

```python
from tkinter import messagebox
```

instead of using only

```python
import tkinter as tk
```

---

### 2.

Which message boxes only display information?

---

### 3.

Which message box returns a boolean?

---

### 4.

Suppose

```python
answer = messagebox.askyesno(...)
```

The user clicks **No**.

What is stored in

```python
answer
```

---

### 5.

Why is

```python
if answer:
```

enough?

Why don't we usually write

```python
if answer == True:
```

---

# 🧩 Mini Exercise (Combining Previous Lessons)

As promised, here's a small exercise that combines several things you've learned.

Build a **Login Window** with:

* A `Frame`
* Username `Entry`
* Password `Entry`
* Your **Show/Hide Password** button from the previous exercise
* A **Login** button

When Login is clicked:

* If username is `"admin"` and password is `"1234"` → show an **information** message box.
* Otherwise → show an **error** message box.

This exercise combines:

* ✅ Frames
* ✅ Labels
* ✅ Entry
* ✅ StringVar
* ✅ Buttons
* ✅ Boolean state
* ✅ `config()`
* ✅ Message boxes

It should fit comfortably in a single Python file and is a great checkpoint before the final lesson on events.

---
