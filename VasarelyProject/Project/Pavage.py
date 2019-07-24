import turtle

from VasarelyProject.Project.FirstStoneHewagoneII import hexagone


def pavage(abscisse_center, ordonnee_center):
    #turtle.up()
    #turtle.goto(-800, 300)
    #turtle.down()
    #abscisse_center = -800
    #ordonnee_center = 300

    for i in range(11):
            #ordonnee_center += 100
            turtle.up()
            turtle.goto(abscisse_center, ordonnee_center)
            turtle.down()
            hexagone("turtle", abscisse_center, ordonnee_center, 50, "Dark Sea Green", "Sea Green", "Medium Sea Green")
            abscisse_center += 150



#pavage(4,56)
