# from turtle import *

# turtle = Turtle()
# turtle.forward(100)

# mainloop()


import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Movement")
screen.setup(width=500, height=500)

# Object 1 set up
obj1 = turtle.Turtle()
obj1.color("red")  # Sets obj1's colour
obj1.speed(1)  # The drawing speed will go as fast as it can if it is set to zero
obj1.penup()  # Don't want it to draw a line as I goes to 0, -50
obj1.goto(0, -50)  # goes to 0, -50
obj1.pendown()  # Now we want it to draw

# Object 2 set up
obj2 = turtle.Turtle()
obj2.color("blue")  # sets obj2's colour
obj2.speed(1)  # The drawing speed will go as fast as it can if it is set to zero
obj2.penup()  # Don't want it to draw a line as I goes to 0, -50
obj2.goto(0, 50)  # goes to 0, 50
obj2.pendown()  # Now we want it to draw

# Movement of objects
while True:  # infinite loop
    obj1.forward(10)  # Moves obj1 forwards by 1
    obj2.forward(10)  # Moves obj2 forwards by 1
