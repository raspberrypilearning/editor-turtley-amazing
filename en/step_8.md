## Rainbow spiral

<div style="border-left: solid; border-width:10px; border-color: #41b653; background-color: #e3f4e6ff; padding: 10px; color: #000000; font-family: inherit;">
We’ll keep using a rectangle in the example code so you can see how each new concept works.  
If you made a different shape in earlier steps, that’s fine — just apply the same ideas to your own shape in the editor! 
</div> 

Now that our spiral can loop through a list of colours forever, let’s make that list **bigger and brighter**.  
We’ll create a rainbow spiral by adding lots of vibrant colours to the list.  

You can use the [Google Colour Picker](https://share.google/KxLnf2VAJCWk2FNuZ) to find RGB values for your own custom colours.

---

### Step 1: Expand the colour list
--- task ---

Replace your current `colours` list with this rainbow list:  

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

colours = [
    (255, 0, 0),     # red
    (255, 165, 0),   # orange
    (255, 255, 0),   # yellow
    (0, 255, 0),     # green
    (0, 127, 255),   # blue
    (0, 0, 255),     # dark blue
    (139, 0, 255)    # violet
]
--- /code ---

--- /task ---

---

### Step 2: Enjoy the rainbow
Your spiral code from Step 8 already uses `colours[i % len(colours)]`, so it will automatically work with this bigger list — no other changes needed.

--- task ---

Run your code to see a rainbow spiral of rectangles.

--- /task ---

---

### Challenge
--- task ---
- [ ] Add even more colours to your list for smoother gradients.  
- [ ] Re‑order the colours to see how it changes the spiral’s look.  
- [ ] Create a “themed” spiral (e.g., shades of blue, sunset colours, etc.).
--- /task ---
