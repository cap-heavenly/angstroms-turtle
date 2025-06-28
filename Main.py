import turtle

# Drawtle (draws grid) and Antle (draws things on grid)
drawtle = turtle.Turtle()
antle = turtle.Turtle()

# Coordinates for each square of the grid + colour (coords[x])
global coords
coords = [(-250.0, -250.0, 'white'), (-250.0, -200.0, 'red'), (-200.0, -200.0, 'white'), (-150.0, -200.0, 'white'), (-100.0, -200.0, 'white'), (-50.0, -200.0, 'white'), (0.0, -200.0, 'white'), (50.0, -200.0, 'white'), (100.0, -200.0, 'white'), (150.0, -200.0, 'white'), (200.0, -200.0, 'white'), (250.0, -200.0, 'white'), (250.0, -150.0, 'white'), (200.0, -150.0, 'white'), (150.0, -150.0, 'white'), (100.0, -150.0, 'white'), (50.0, -150.0, 'white'), (0.0, -150.0, 'white'), (-50.0, -150.0, 'white'), (-100.0, -150.0, 'white'), (-150.0, -150.0, 'white'), (-200.0, -150.0, 'white'), (-250.0, -150.0, 'white'), (-250.0, -100.0, 'white'), (-200.0, -100.0, 'white'), (-150.0, -100.0, 'white'), (-100.0, -100.0, 'white'), (-50.0, -100.0, 'white'), (0.0, -100.0, 'white'), (50.0, -100.0, 'white'), (100.0, -100.0, 'white'), (150.0, -100.0, 'white'), (200.0, -100.0, 'white'), (250.0, -100.0, 'white'), (250.0, -50.0, 'white'), (200.0, -50.0, 'white'), (150.0, -50.0, 'white'), (100.0, -50.0, 'white'), (50.0, -50.0, 'white'), (0.0, -50.0, 'white'), (-50.0, -50.0, 'white'), (-100.0, -50.0, 'white'), (-150.0, -50.0, 'white'), (-200.0, -50.0, 'white'), (-250.0, -50.0, 'white'), (-250.0, 0.0, 'white'), (-200.0, 0.0, 'white'), (-150.0, 0.0, 'white'), (-100.0, 0.0, 'white'), (-50.0, 0.0, 'white'), (0.0, 0.0, 'white'), (50.0, 0.0, 'white'), (100.0, 0.0, 'white'), (150.0, 0.0, 'white'), (200.0, 0.0, 'white'), (250.0, 0.0, 'white'), (250.0, 50.0, 'white'), (200.0, 50.0, 'white'), (150.0, 50.0, 'white'), (100.0, 50.0, 'white'), (50.0, 50.0, 'white'), (0.0, 50.0, 'white'), (-50.0, 50.0, 'white'), (-100.0, 50.0, 'white'), (-150.0, 50.0, 'white'), (-200.0, 50.0, 'white'), (-250.0, 50.0, 'white'), (-250.0, 100.0, 'white'), (-200.0, 100.0, 'white'), (-250.0, 200.0, 'white'), (-200.0, 200.0, 'white'), (-150.0, 200.0, 'white'), (-100.0, 200.0, 'white'), (-50.0, 200.0, 'white'), (0.0, 200.0, 'white'), (50.0, 200.0, 'white'), (100.0, 200.0, 'white'), (150.0, 200.0, 'white'), (200.0, 200.0, 'white'), (250.0, 200.0, 'white'), (250.0, 250.0, 'white'), (200.0, 250.0, 'white'), (150.0, 250.0, 'white'), (100.0, 250.0, 'white'), (50.0, 250.0, 'white'), (0.0, 250.0, 'white'), (-50.0, 250.0, 'white'), (-100.0, 250.0, 'white'), (-150.0, 250.0, 'white'), (-200.0, 250.0, 'white'), (-250.0, 250.0, 'white'), (-200.0, -250.0, 'white'), (-150.0, -250.0, 'white'), (-100.0, -250.0, 'white'), (-50.0, -250.0, 'white'), (0.0, -250.0, 'white'), (50.0, -250.0, 'white'), (100.0, -250.0, 'white'), (150.0, -250.0, 'white'), (200.0, -250.0, 'white'), (250.0, -250.0, 'white'), (-200.0, 100.0, 'white'), (-150.0, 100.0, 'white'), (-100.0, 100.0, 'white'), (-50.0, 100.0, 'white'), (0.0, 100.0, 'white'), (50.0, 100.0, 'white'), (100.0, 100.0, 'white'), (150.0, 100.0, 'white'), (200.0, 100.0, 'white'), (250.0, 100.0, 'white'), (250.0, 150.0, 'white'), (200.0, 150.0, 'white'), (150.0, 150.0, 'white'), (100.0, 150.0, 'white'), (50.0, 150.0, 'white'), (0.0, 150.0, 'white'), (-50.0, 150.0, 'white'), (-100.0, 150.0, 'white'), (-150.0, 150.0, 'white'), (-200.0, 150.0, 'white'), (-250.0, 150.0, 'white')]
def goooo(whichtle, x, y):
    whichtle.speed(0)
    whichtle.penup()
    whichtle.goto(x, y)
    whichtle.seth(0)
    whichtle.pendown()
    
def draw_grid():
    goooo(drawtle, -250, -250)
    drawtle.speed(0)
    drawtle.left(90)
    for i in range(5):
        print(drawtle.position())
        drawtle.forward(50)
        print(drawtle.position())
        drawtle.right(90)
        drawtle.forward(500)
        drawtle.left(90)
        drawtle.forward(50)
        drawtle.left(90)
        drawtle.forward(500)
        drawtle.right(90)
    for i in range(5):
        drawtle.right(90)
        drawtle.forward(50)
        drawtle.right(90)
        drawtle.forward(500)
        drawtle.left(90)
        drawtle.forward(50)
        drawtle.left(90)
        drawtle.forward(500)

def coord_blot():
    drawtle.speed(0)
    for i in range(len(coords)):
        goooo(drawtle, coords[i][0], coords[i][1])
        drawtle.dot(6, "red")


def square_fill(colour, angle):
    antle.speed(0)
    antle.penup()
    antle.seth(0)
    antle.forward(25)
    antle.left(90)
    antle.forward(25)
    antle.right(180)
    antle.pendown()
    antle.fillcolor(colour)
    antle.begin_fill()
    for i in range(4):
        antle.forward(50)
        antle.right(90)
    antle.end_fill()
    antle.penup()
    antle.forward(25)
    antle.right(90)
    antle.forward(25)
    antle.seth(0)
    for i in range(len(coords)):
        if int(coords[i][0]) == round(antle.ycor()-25, 0) and int(coords[i][1]) == round(antle.xcor()-25, 0):
            coords[i] = (coords[i][0], coords[i][1], colour)
            print(f"Filled square at {coords[i][0]}, {coords[i][1]} with {colour}")
            break
        print(f"{coords[i][0], coords[i][1], antle.xcor(), antle.ycor()}")
    antle.seth(angle)
    
def colour_check():
    for i in range(len(coords)):
        if coords[i][0] == round(antle.ycor()-25, 0) and coords[i][1] == round(antle.xcor()-25, 0):
            return coords[i][2]
            break
        print(f"{coords[i][0], coords[i][1], antle.xcor(), antle.ycor()}")

def coord_move(dy, dx):
    antle.penup()
    antle.seth(0)
    antle.forward(50*dy)
    antle.right(90)
    antle.forward(50*-dx)
    antle.seth(0)

def smiley():
    square_fill("black", antle.heading())
    coord_move(-3, 0)
    square_fill("black", antle.heading())
    coord_move(0, -2)
    square_fill("black", antle.heading())
    coord_move(1, -1)
    square_fill("black", antle.heading())
    coord_move(1, 0)
    square_fill("black", antle.heading())
    coord_move(1, 1)
    square_fill("black", antle.heading())

def heart():
    square_fill("red", antle.heading())
    coord_move(0, -1)
    square_fill("red", antle.heading())
    coord_move(1, 0)
    square_fill("red", antle.heading())
    coord_move(0, -1)
    square_fill("red", antle.heading())
    coord_move(1, 1)
    square_fill("red", antle.heading())
    coord_move(0, 1)
    square_fill("red", antle.heading())

def the_ant():
    for i in range(1000):
        antle.speed(1)
        antle.penup()
        if colour_check() == "white":
            square_fill("black", antle.heading())
            antle.right(90)
            antle.forward(50)
        elif colour_check() == "black":
            square_fill("white", antle.heading())
            antle.left(90)
            antle.forward(50)
    

s = antle.getscreen()
s.setup(width=500, height=500)
drawtle.hideturtle()
goooo(antle, 25, 25)
draw_grid()
#coord_blot()
goooo(antle, -175, -225)
print(colour_check())
#the_ant()

#square_fill("black", anlte.heading())
#square_fill("white")
#smiley()
#print(coords)
#coord_move(0, 6)
#heart()
antle.screen.exitonclick()


