from turtle import Turtle

turtle = Turtle()

R = 0
G = 0
B = 255

turtle.speed(0)

number_of_shapes = 80

for j in range(number_of_shapes):
    for i in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
        R = (R + 5) % 256
        G = (G + 2) % 256
        B = (B - 3) % 256
        turtle.color((R / 255, G / 255, B / 255))
    turtle.right(360 / number_of_shapes)
