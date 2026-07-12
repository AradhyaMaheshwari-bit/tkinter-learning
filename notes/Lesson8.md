# Lesson 8 — `sticky`

Now we learn the last major layout concept.

Suppose you have this grid:

```text
+---------+
|         |
|    A    |
|         |
+---------+
```

Notice that the label is **centered** inside its cell.

What if you wanted it in the top-left corner?

Or stretched across the whole cell?

That's what `sticky` controls.

---

## What does `sticky` mean?

Think of it as:

> "Which sides of the cell should this widget stick to?"

Possible values:

```python
sticky="n"
sticky="s"
sticky="e"
sticky="w"
```

These are compass directions.

```
      N
      ↑
W ←       → E
      ↓
      S
```

* `n` = North (top)
* `s` = South (bottom)
* `e` = East (right)
* `w` = West (left)

---

## Example 1

```python
tk.Label(root, text="A").grid(
    row=0,
    column=0,
    sticky="w"
)
```

The label moves to the **left side of its grid cell**.

Instead of:

```text
+---------+
|         |
|    A    |
|         |
+---------+
```

you get:

```text
+---------+
|A        |
|         |
|         |
+---------+
```

---

## Example 2

```python
sticky="e"
```

```text
+---------+
|        A|
|         |
|         |
+---------+
```

---

## Example 3

```python
sticky="n"
```

```text
+---------+
|    A    |
|         |
|         |
+---------+
```

---

## Combining Directions

You can combine them.

```python
sticky="nw"
```

Top-left.

```text
+---------+
|A        |
|         |
|         |
+---------+
```

or

```python
sticky="se"
```

Bottom-right.

---

## Stretching

Remember `fill` in `pack()`?

`grid()` uses `sticky` instead.

```python
sticky="ew"
```

means:

Stick to the **East** and **West** edges.

The widget stretches horizontally.

```text
+---------+
|AAAAAAAAA|
+---------+
```

Similarly,

```python
sticky="ns"
```

stretches vertically.

And

```python
sticky="nsew"
```

stretches in all directions to fill the cell.

---

## Think of It This Way

* `pack(fill="x")` → Fill horizontally.
* `grid(sticky="ew")` → Stretch horizontally inside the grid cell.

Different syntax, same goal.

---

# Experiments

### Experiment 1

Predict:

```python
tk.Label(
    root,
    text="A",
    bg="yellow"
).grid(
    row=0,
    column=0,
    sticky="w"
)
```

Where will **A** appear inside its cell?

---

### Experiment 2

Predict:

```python
sticky="nsew"
```

What do you think happens to the label?

---

## Questions

1. What does `sticky` control?
2. Why are the letters `n`, `s`, `e`, and `w` used?
3. What's the difference between `sticky="w"` and `sticky="ew"`?
4. How would you make a widget fill the entire grid cell?
