<h2 class="c-project-heading--task">Turning</h2>
--- task ---

Make the turtle turn around.

--- /task ---

To turn the turtle, it has to move forward and turn right (or left). 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---
from turtle import Turtle

turtle = Turtle()

turtle.forward(100)
turtle.right(90)
turtle.forward(60)
--- /code ---
</div>

--- task ---

Click **Run** to see your new changes.

--- /task ---

<div class="c-project-output">

![A path formed by a line to the right, then angled downwards](images/turn.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- `turtle.right(90)` turns the cursor 90 degrees right. 
- `turtle.left(90)` turns the cursor 90 degrees left.

</div>
