## Turning

You've used code to draw a line. Good work! Now let's try making the turtle turn around. To do this you need to instruct the turtle not only to move forward, but also to turn right or left. 

--- task ---

Add this line to the bottom of your script:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7-8
---
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
--- /code ---

--- /task ---

--- task ---

Run your code. What happens?

--- /task ---

`turtle.right(90)` turns the cursor 90 degrees right. You can also turn left with `turtle.left(90)`. To change the amount that the cursor turns, simply change the number of degrees. 

--- task ---

Complete the square shape you've started by adding the next lines of code and press ![arrow](images/arrow.png). Keep trying until you get it right. 

--- /task ---

--- task ---
### Experiment
Try to draw all of these shapes, to become a true shape master:

- [ ] Draw a rectangle (two of the four sides need to be longer)
- [ ] Draw a triangle (how many degrees do you need to turn?)
- [ ] Draw a cross (`backward` and `forward` work well together)
- [ ] Draw a circle (what happens if you turn a small amount lots of times, and move forward a tiny bit each time?) 

--- /task ---

In the next step, add colour to your shape!