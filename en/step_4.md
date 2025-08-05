## Changing colours

<div style="border-left: solid; border-width:10px; border-color: #41b653; background-color: #e3f4e6ff; padding: 10px; color: #000000; font-family: inherit;">
In the next few steps, we’ll keep using a rectangle in the example code so you can see how each new concept works.  
If you made a different shape in earlier steps, that’s fine — just apply the same ideas to your own shape in the editor! 
</div> 

Right now our example rectangle is drawn in the default black pen on a white background. Let’s brighten things up by adding colour.  

We’ll use **RGB values** to pick colours. RGB stands for **Red**, **Green**, and **Blue** — each can be set from `0` (none) to `255` (full).  

--- task ---

Add this code **before** your `turtle.forward(…)` lines to give your shape a bright blue pen colour:  

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6-10
---
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)
R = 0
G = 0
B = 255
turtle.color((R, G, B))

# Rectangle example
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
--- /code ---

Run your code in the editor to see your shape drawn in blue.

--- /task ---

You can change the colour by adjusting the `R`, `G`, and `B` values. For example:  
- `(255, 0, 0)` = bright red  
- `(0, 255, 0)` = bright green  
- `(255, 255, 0)` = yellow  


--- task ---

### Experiment

- [ ] Change the pen colour to your favourite colour.  
- [ ] Draw the rectangle again with each side in a **different colour**.  

--- /task ---
