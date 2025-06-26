import turtle
def goooo(x, y):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.seth(0)
    turtle.forward(y)
    turtle.seth(90)
    turtle.forward(x)
    turtle.seth(0)
    turtle.pendown()
def draw_grid():
    goooo(-500, -500)
    turtle.speed(3)
    for i in range(5):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(500)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(500)
        turtle.right(90)

    turtle.hideturtle()

s = turtle.getscreen()
s.setup(width=500, height=500)


draw_grid()

