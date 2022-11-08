import math
from time import sleep
from turtle import *

screen = Screen()
# screen.setup(height=350)

def draw_star(t: Turtle = None, size: int = None, points: int = 5, angle: int = 0, thickness: int = None, fill: bool = False):
    if not size : raise Exception(f"Size '{size}' is an invalid size")

    if not t: t = Turtle()

    origin = t.position()
    heading = t.heading()
    # print(f"origin {origin} , angle {heading}")

    rayon = size/2

    t.penup()
    t.left(90)
    t.right(angle)
    t.forward(rayon)
    t.right(180)
    t.pendown()

    angle_branches = 360/(points)
    angle_interne = angle_thickness = cote_pointes_demis = None

    # pour travailler sur l'epaisseur de l'etoile 
    if not thickness or thickness < 0 or thickness > 1 :
        print("not thickness", angle_branches, angle_branches/30, angle_branches/(angle_branches/30))
        angle_interne = (180 - angle_branches*2)/2 if points%2 == 1 and points > 3 else angle_branches/(angle_branches/30) if points > 3 else angle_branches/(angle_branches/20)
        angle_thickness = 180 - (angle_branches/2) - angle_interne
        cote_pointes_demis = (rayon/math.sin(math.radians(angle_thickness))) * math.sin(math.radians(angle_branches/2))
    else :
        print("thickness", thickness)
        pass

    # Relis les pointes avec l'angle interne suivant l'epaisseur
    if fill : t.begin_fill()
    # t.right(180 - angle_interne)
    for _ in range(points):
        t.left(angle_interne)
        # t.left(180 - angle_interne)
        t.forward(cote_pointes_demis)
        t.left(angle_thickness*2 - 180)
        t.forward(cote_pointes_demis)
        t.right(180 - angle_interne)
    if fill : t.end_fill()

    # Fin draw star
    t.penup()
    t.goto(origin)
    t.setheading(heading)
    t.pendown()
    # print(f"origin {t.position()} , angle {t.heading()}")


size = 100
space_ratio = 1.3
# r = range (2, 12)
r = range (5, 8)

# draw_star(size=150)
# mainloop()
# exit()

t = Turtle()
t.speed(0)
t.penup()
decalage = (len(r)*size*space_ratio - size*space_ratio)/2
screen.setup(width=(decalage + size*space_ratio)*2, height=size*(1+space_ratio))
# t.goto(decalage, 0)
t.goto(-decalage, 0)
t.pendown()

for nb in r :
    print(f"--- étoile {nb}")
    t.color("black")
    t.penup()
    t.setheading(270)
    t.forward(size/2)
    t.pendown()
    t.left(90)
    t.circle(size/2)
    t.penup()
    t.left(90)
    t.forward(size/2)
    t.right(90)
    t.pendown()
    # t.color("yellow")
    t.pen(pencolor="orange", fillcolor="yellow")
    # draw_star(t, size = size, points = nb, fill = True)
    draw_star(t, size=size, points=nb, thickness=.5, fill=True)
    # break # TODO : Remove
    # sleep(1)
    t.penup()
    t.forward(size*space_ratio)
    t.pendown()

mainloop()