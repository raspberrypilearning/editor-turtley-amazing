
## Modulo to the rescue!

<div style="border-left: solid; border-width:10px; border-color: #41b653; background-color: #e3f4e6ff; padding: 10px; color: #000000; font-family: inherit;">
We’ll keep using a rectangle in the example code so you can see how each new concept works.  
If you made a different shape in earlier steps, that’s fine — just apply the same ideas to your own shape in the editor! 
</div> 

In the last step, your spiral worked for a while, then crashed with:

```

IndexError: list index out of range

```

This happens because the loop’s counter `i` keeps going up, but our colour list only has a limited number of items.  
When `i` is bigger than the last position in the list, Python doesn’t know which colour to use.

---

### The modulo operator
The **modulo** operator `%` finds the **remainder** after division.  

For example:  
- `7 % 3` is `1` (because 3 goes into 7 twice, with 1 left over).  
- `12 % 5` is `2` (because 5 goes into 12 twice, with 2 left over).  

We can use `%` to make `i` loop back to `0` when it reaches the end of the list.

---

### Step 1: Apply modulo to our colour choice
--- task ---

Change the colour line in your inner loop so it wraps `i` with modulo:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 20
---
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)
R = 0
G = 0
B = 255
turtle.color((R, G, B))

colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

for j in range(30):
    for i in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.color(colours[i % len(colours)])
    turtle.right(10)
--- /code ---

--- /task ---

--- task ---

Run your code — now the colours repeat endlessly without an error.

--- /task ---

--- task ---
### Experiment
- [ ] Try different numbers of colours in your list — the modulo will keep working.  
- [ ] Make a “rainbow” spiral by adding lots of bright colours.
--- /task ---