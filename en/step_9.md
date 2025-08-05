## More experiments

<div style="border-left: solid; border-width:10px; border-color: #ff9800; background-color: #fff3e0; padding: 10px; color: #000000; font-family: inherit;">
The following activities are **optional extras**.  
They will replace your current rectangle spiral code if you run them, so make a copy of your finished script first if you want to keep it.  
These examples are just for fun — explore and see what patterns you can make!
</div> 

---

### Experiment 1: Better spirals
This experiment creates a very different spiral pattern by using a single long loop, adjusting the RGB values each time.

--- task ---

Replace your current code with this and run it:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
---
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.bgcolor((255, 255, 255))
screen.colormode(255)

R = 255
G = 0
B = 0

for i in range(2000):
    G += 1
    B += 0.5
    R -= 1
    turtle.color((R, G, B))
    turtle.forward(i)
    turtle.right(98)
--- /code ---

--- /task ---

Try changing the turn angle in `turtle.right(98)` and see how the spiral changes.

---

### Experiment 2: While‑loop rainbow spiral
This experiment uses **while loops** to generate a long list of colours and then loops through them to draw a complex spiral.

--- task ---

Replace your current code with this and run it:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
---
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
#screen.colormode(255)

R = 255
G = 0
B = 0

screen.bgcolor((0, 0, 255))

turtle.speed(0)

colours = []

while G <= 255:
    colours.append((R, G, B))
    G += 1

while R >= 0:
    colours.append((R, G, B))
    R -= 1

while B < 255:
    colours.append((R, G, B))
    B += 1

while G > 0:
    colours.append((R, G, B))
    G -= 1

while R < 255:
    colours.append((R, G, B))
    R += 1
  

for i in range(3000):
    turtle.color(colours[i % len(colours)])
    turtle.forward(i/3)
    turtle.right(119)
--- /code ---

--- /task ---

---


--- task ---
### Experiment
- [ ] Combine ideas from both experiments to create a unique pattern.  
- [ ] Change the turn angles, colours, or shapes to make something completely new.
--- /task ---
