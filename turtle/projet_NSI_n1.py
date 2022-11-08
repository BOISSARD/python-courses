# This is a sample Python script.
from turtle import *
t=Turtle()
t.speed(0)
t.pen(pencolor="red", fillcolor="red")
largeur_drapeau=100
hauteur_bande=20

#positionnement au point de départ
t.penup()
t.goto(-largeur_drapeau/2,-hauteur_bande*13/2) #positionnement du curseur pour centrer le dessin
t.pendown()


#on va tracer nos 7 bande rouge
for i in range(7):
    t.begin_fill()
    t.fd(largeur_drapeau)
    t.left(90)
    t.fd(hauteur_bande)
    t.left(90)
    t.fd(largeur_drapeau)
    t.left(90)
    t.fd(hauteur_bande)
    t.left(90)
    t.end_fill()
    #positionnement du curseur pour la ligne suivante
    t.penup()
    t.left(90)
    t.fd(hauteur_bande * 2)
    t.rt(90)
    t.pendown()

#place le curseur pour faire le rectangle bleu
hauteur_rectangle_bleu=hauteur_bande*7
largeur_rectangle_bleu=largeur_drapeau*2/5
t.penup()
t.goto(-largeur_drapeau/2, hauteur_bande*13/2)
t.pendown()

#trace le rectangle bleu
t.pen(pencolor="blue", fillcolor="blue")
t.begin_fill()
t.fd(largeur_rectangle_bleu)
t.right(90)
t.fd(hauteur_rectangle_bleu)
t.rt(90)
t.fd(largeur_rectangle_bleu)
t.rt(90)
t.fd(hauteur_rectangle_bleu)
t.end_fill()


t.penup()
#ici on definie le rayon de l'etoile
rayon_etoile=0
print(hauteur_rectangle_bleu/11, largeur_rectangle_bleu/13)
if hauteur_rectangle_bleu/11 < largeur_rectangle_bleu/13:
    rayon_etoile = hauteur_rectangle_bleu/11
else:
    rayon_etoile = largeur_rectangle_bleu/13
print(rayon_etoile)

#ici on trace les etoiles
t.pen(pencolor="white", fillcolor="white")
t.backward(hauteur_rectangle_bleu/11 + rayon_etoile)
t.rt(90)
t.fd(largeur_rectangle_bleu/13 + rayon_etoile)
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




mainloop()
