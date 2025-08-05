## Loopy colours

<div style="border-left: solid; border-width:10px; border-color: #41b653; background-color: #e3f4e6ff; padding: 10px; color: #000000; font-family: inherit;">
We’ll keep using a rectangle in the example code so you can see how each new concept works.  
If you made a different shape in earlier steps, that’s fine — just apply the same ideas to your own shape in the editor! 
</div> 

So far, we’ve been changing the RGB values ourselves to shift colours.  
Now we’ll store a set of colours in a **list** and loop through them.

A list in Python is written in square brackets `[ ]`, with each item separated by a comma.  
Each colour here is an **RGB tuple** like `(255, 0, 0)`.

---


--- task ---
### Step 1: Create a list of colours
Add this list of colours to your script **above** the outer loop:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 11
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
--- /code ---

--- /task ---

---


--- task ---
### Step 2: Use the list in your spiral
Change the line where you set the turtle’s colour in the **inner loop** so it uses the list:  

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
        turtle.color(colours[i])
    turtle.right(10)
--- /code ---

--- task ---

Run your code — you’ll see your spiral change colour using the list.  
After a while, the program will crash with an **IndexError: list index out of range**.
We’ll fix it in the next step so it can loop through the colours forever.

--- /task ---

--- /task ---

--- task ---
### Experiment
- [ ] Add more colours to your list and see how far you can get before the error happens.
- [ ] Try making your own custom colour combinations.
--- /task ---
