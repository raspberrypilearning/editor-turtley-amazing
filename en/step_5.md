## Loops and colour changes

<div style="border-left: solid; border-width:10px; border-color: #41b653; background-color: #e3f4e6ff; padding: 10px; color: #000000; font-family: inherit;">
We’ll keep using a rectangle in the example code so you can see how each new concept works.  
If you made a different shape in earlier steps, that’s fine — just apply the same ideas to your own shape in the editor! 
</div> 

Our blue rectangle works, but the code repeats the same instructions for each side.  
With a **loop**, we can make the turtle draw shapes faster — and by nesting loops we can create exciting spirals.  

---

### Step 1: A loop for one rectangle
We’ll start by making the turtle draw the rectangle using a single loop.

--- task ---

Replace your movement lines with this code:  

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 12-15
---
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)
R = 0
G = 0
B = 255
turtle.color((R, G, B))

for i in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
--- /code ---

Run your code — you should see the same blue rectangle, but with shorter, tidier code.

--- /task ---

---

### Step 2: Repeat the rectangle in a spiral
Now let’s wrap that rectangle loop in another loop.  
The outer loop will draw the rectangle many times, turning a little after each one.

--- task ---

Add an **outer loop** and a small turn after each rectangle:  

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 12,18
---
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)
R = 0
G = 0
B = 255
turtle.color((R, G, B))

for j in range(30):
    for i in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
--- /code ---

Run your code — now you have 30 blue rectangles rotated to make a spiral.

--- /task ---

---

### Step 3: Add colour changes
Finally, we’ll change the `R`, `G`, and `B` values inside the inner loop so the spiral shifts colour as it draws.

--- task ---

Insert the colour change lines before `turtle.color((R, G, B))` in the **inner loop**:  

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 18-21
---
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)
R = 0
G = 0
B = 255
turtle.color((R, G, B))

for j in range(30):
    for i in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        R = (R + 5) % 256
        G = (G + 2) % 256
        B = (B - 3) % 256
        turtle.color((R, G, B))
    turtle.right(10)
--- /code ---

Run the code again — now your spiral changes colour with each rectangle.

--- /task ---

--- task ---
### Experiment

Change the turn amount in `turtle.right(10)` to make tighter or looser spirals.
- [ ] Try different numbers for `R`, `G`, and `B` changes to see new colour blends.
- [ ] Swap the rectangle for another shape and see how the spiral changes.

--- /task ---

--- hints ---
--- hint ---
To make the colour shift faster, increase the numbers you add or subtract from `R`, `G`, or `B`.
--- /hint ---
--- hint ---
To slow the colour change, use smaller numbers like `+1` or `-1`.
--- /hint ---
--- /hints ---
