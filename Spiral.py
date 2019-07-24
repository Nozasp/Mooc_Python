import turtle


def spirale(a, b, c):
    turtle.shape(a)
    turtle.down()
    turtle.color(b)
    turtle.width(c)
    for i in range(100):
        turtle.circle(i*(c/2), 90) # (rayon, angle)

    turtle.done()
    while True:
        turtle.reset()
        turtle.speed(0)
        spirale(turtle, "red", 10)


x = input("Outil shape (turtle)" )
y = input("Color :")
z = int(input("épaisseur (10) : "))

print(spirale(x, y, z))
