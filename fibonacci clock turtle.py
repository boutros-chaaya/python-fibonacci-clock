import turtle
from datetime import datetime

now = datetime.now()


def carre(x, y, cote):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.speed(0)
    turtle.pencolor('black')
    for i in range(4):
        turtle.forward(cote)
        turtle.left(90)


def carreNumero(n):
    if n == 0:
        carre(90, 0, 150)
    elif n == 1:
        carre(0, 0, 90)
    elif n == 2:
        carre(0, 90, 60)
    elif n == 3:
        carre(60, 90, 30)
    elif n == 4:
        carre(60, 120, 30)


listecarre = [5, 3, 2, 1, 1]
listeH = [0, 0, 0, 0, 0]
listeM = [0, 0, 0, 0, 0]


def temps(h, m):
    m = int(m / 5)
    for i in range(5):
        if h >= listecarre[i]:
            listeH[i] = 1
            h = h - listecarre[i]
        if m >= listecarre[i]:
            listeM[i] = 1
            m = m - listecarre[i]

    for i in range(5):
        if listeH[i] + listeM[i] == 2:
            turtle.color("blue")
        if listeH[i] == 1 and listeM[i] == 0:
            turtle.color("red")
        if listeH[i] == 0 and listeM[i] == 1:
            turtle.color("green")
        if listeH[i] + listeM[i] == 0:
            turtle.color("white")

        turtle.begin_fill()
        carreNumero(i)
        turtle.end_fill()


# Programme principal
if now.hour > 12:
    h = now.hour - 12

temps(h, now.minute)
turtle.done()
