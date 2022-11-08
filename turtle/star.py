import math
from time import sleep
from turtle import *

screen = Screen()
# screen.setup(height=350)
screen.setup(width=1200, height=350)

def draw_star(t: Turtle = None, size: int = None, points: int = 5, angle: int = 0, thickness: int = None, fill: bool = False):
    if not size : raise Exception(f"Size '{size}' is an invalid size")

    if not t: t =Turtle()

    origin = t.position()
    heading = t.heading()
    # print(origin, t.heading())

    rayon = size/2

    t.penup()
    t.left(90)
    t.forward(rayon)
    t.right(180)
    t.pendown()

    angle_branches = 360/(points)
    # print(angle_branches, angle_branches*points)

    # Trace les droites des branches
    # for i in range(points):
    #     t.forward(rayon)
    #     t.left(180 - angle_branches)
    #     t.forward(rayon)
    #     t.right(180)

    angle_pointe = angle_interne = angle_branches

    # pour travailler sur l'epaisseur de l'etoile 
    if not thickness or thickness < 0 or thickness > 1 :
        angle_pointe = (180 - angle_branches*2)/2
        print("not thickness", angle_branches, angle_branches/15, angle_branches/(angle_branches/15))
        angle_interne = (180 - angle_branches*2)/2 if points%2 == 1 and points > 3 else angle_branches/(angle_branches/15)
    else :
        print("thickness", thickness)
        pass

    # print(f"angle_branches {angle_branches}", f"angle_pointe {angle_pointe}", f"angle_interne {angle_interne}")

    # Relis les pointes
    cote_pointes = math.sin(math.radians((180 - angle_branches)/2)) * rayon * 2
    # sleep(0.5)
    # for i in range(points):
    #     t.left(angle_branches/2)
    #     t.forward(cote_pointes)
    #     t.right((360 - angle_branches)/2)


    # Relis les pointes 1/2, fait un tour si impair sinon la moitié de la figure
    # cote_pointes_doubles = math.sin(math.radians((180 - angle_pointe*2)/2)) * rayon * 2
    # sleep(0.5)
    # for i in range(points):
    #     t.right(angle_pointe)
    #     t.forward(cote_pointes_doubles)
    #     t.left((360 - angle_pointe*2)/2)
    #     pass

    # Relis les pointes avec l'angle interne
    angle_thickness = 180 - (angle_branches/2) - angle_interne
    # print("angles centre", angle_branches/2, "angle pointe", angle_interne, "angle thickness", angle_thickness)
    cote_pointes_demis = (rayon/math.sin(math.radians(angle_thickness))) * math.sin(math.radians(angle_branches/2))
    # print(cote_pointes_demis)
    sleep(0.5)
    if fill : t.begin_fill()
    for i in range(points):
        t.left(angle_interne)
        t.forward(cote_pointes_demis)
        t.right(180 + 360 - angle_thickness*2)
        t.forward(cote_pointes_demis)
        t.right(180 - angle_interne)
    if fill : t.end_fill()

    # Fin draw star
    t.penup()
    t.goto(origin)
    t.setheading(heading)
    t.pendown()

size = 100
r = range (2, 8)
# r = range (5, 8)

draw_star()

t = Turtle()
t.speed(0)
t.penup()
t.goto(-((len(r)*2 -1)*size)/2 + size/2, 0)
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
    draw_star(t, size = size, points = nb, fill = True)
    # break # TODO : Remove
    sleep(1)
    t.penup()
    t.forward(size*2)
    t.pendown()

mainloop()