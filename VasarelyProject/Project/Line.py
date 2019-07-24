import turtle
from VasarelyProject.Project.Pavage import pavage


def line(ordonnee_center, ordonnee_centerII):
    for i in range(2):
        if i % 2 != 0:
            pavage(-775, ordonnee_center)

        if i % 2 == 0:
            pavage(-700, ordonnee_centerII)


#line()

def multiLine(ordonnee_center, ordonnee_centerII):
    for i in range(15):
        print(i)
        if i == 0:
            ordonnee_center = 455
            ordonnee_centerII = 500
            line(ordonnee_center, ordonnee_centerII)

        if i > 0:
            ordonnee_center -= 85
            ordonnee_centerII -= 85
            line(ordonnee_center, ordonnee_centerII)

    turtle.done()


multiLine(255, 300)