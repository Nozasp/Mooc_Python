import turtle


def hexagone ( t, abscisse_centre, ordonnee_centre, longueur_arrete, color1, color2, color3):
    turtle.shape(t)
    turtle.speed("fastest")
    for i in range(3):
        angle = 120
        turtle.begin_fill()
        turtle.up()
        turtle.goto(abscisse_centre, ordonnee_centre)
        turtle.down()
        if i == 0:
            turtle.color(color1)
        elif i == 1:
            turtle.color(color2)
        elif i == 2:
            turtle.color(color3)
        for j in range(4):  # chaques itération trace un losange
            turtle.forward(longueur_arrete)
            turtle.left(angle)
            angle = 180 - angle
        turtle.right(120)
        turtle.end_fill()
    #turtle.hideturtle()
    #turtle.done()


#hexagone('turtle', int(input()), int(input()), int(input()), "Dark Sea Green", "Sea Green", "Medium Sea Green")
