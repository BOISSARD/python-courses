from turtle import *

screen = Screen()
# screen.screensize(bg="black")

LARGEUR_DRAPEAU = 600
HAUTEUR_BANDE = 20
DEBUG = False

turtles_bandes = [Turtle() for i in range(7)]

for i, t in enumerate(turtles_bandes):
    t.pen(pencolor="red", fillcolor="red")
    t.speed(0)
    t.penup()
    t.goto(-LARGEUR_DRAPEAU/2, -HAUTEUR_BANDE*13/2 + i*HAUTEUR_BANDE*2)
    t.pendown()
    t.begin_fill()


step = 10
r = LARGEUR_DRAPEAU/step
for i in range(round(r)):
    for t in turtles_bandes:
        t.forward(step)

for t in turtles_bandes:
    t.left(90)

r = HAUTEUR_BANDE/step
for i in range(round(r)):
    for t in turtles_bandes:
        t.forward(step)

for t in turtles_bandes:
    t.left(90)

r = LARGEUR_DRAPEAU/step
for i in range(round(r)):
    for t in turtles_bandes:
        t.forward(step)

for t in turtles_bandes:
    t.left(90)

r = HAUTEUR_BANDE/step
for i in range(round(r)):
    for t in turtles_bandes:
        t.forward(step)


for t in turtles_bandes:
    t.hideturtle()

for i, t in enumerate(turtles_bandes):
    t.end_fill()

#place le curseur pour faire le rectangle bleu
t = Turtle()
t.pen(pencolor="blue", fillcolor="blue")
t.penup()
t.goto(-LARGEUR_DRAPEAU/2, HAUTEUR_BANDE*13/2)
t.pendown()

hauteur_rectangle_bleu = HAUTEUR_BANDE*7
largeur_rectangle_bleu = LARGEUR_DRAPEAU*2/5

#trace le rectangle bleu
t.begin_fill()
t.fd(largeur_rectangle_bleu)
t.right(90)
t.fd(hauteur_rectangle_bleu)
t.rt(90)
t.fd(largeur_rectangle_bleu)
t.rt(90)
t.fd(hauteur_rectangle_bleu)
t.end_fill()
t.hideturtle()

if DEBUG :
    t = Turtle()
    t.speed(0)
    t.penup()
    t.goto(-LARGEUR_DRAPEAU/2, HAUTEUR_BANDE*13/2)
    t.pendown()
    t.pen(pencolor="black", fillcolor="black")
    for i in range(13) :
        t.fd(largeur_rectangle_bleu/13)
        if i%2 == 0 : t.right(90)
        else : t.left(90)
        t.fd(hauteur_rectangle_bleu)
        if i%2 == 1 : t.right(90)
        else : t.left(90)
    t.right(180)
    for i in range(11):
        t.fd(largeur_rectangle_bleu)
        if i%2 == 0 : t.right(90)
        else : t.left(90)
        t.fd(hauteur_rectangle_bleu/11)
        if i%2 == 0 : t.right(90)
        else : t.left(90)
    t.hideturtle()

# place le curseur pour faire les étoiles
t = Turtle()
t.pen(pencolor="white", fillcolor="white")
t.penup()
t.goto(-LARGEUR_DRAPEAU/2, HAUTEUR_BANDE*13/2)

# ici on definie le rayon de l'etoile
rayon_etoile = 0
if hauteur_rectangle_bleu/11 < largeur_rectangle_bleu/13:
    rayon_etoile = hauteur_rectangle_bleu/11
else:
    rayon_etoile = largeur_rectangle_bleu/13

#ici on trace les etoiles
t.pen(pencolor="white", fillcolor="white")
t.rt(90)
t.fd(1.5*hauteur_rectangle_bleu/11)
t.lt(90)
t.fd(1.5*largeur_rectangle_bleu/13)

for i in range(9):
    for j in range(6 if i % 2 == 0 else 5):
        t.dot(rayon_etoile)
        t.fd(2*largeur_rectangle_bleu/13)
    if i % 2 == 0:
        t.rt(90)
        t.fd(hauteur_rectangle_bleu/11)
        t.rt(90)
        t.fd(3*largeur_rectangle_bleu/13)
    else:
        t.backward(largeur_rectangle_bleu/13)
        t.lt(90)
        t.fd(hauteur_rectangle_bleu/11)
        t.lt(90)
t.hideturtle()

mainloop()
