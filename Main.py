import turtle
import random
# Drawtle (draws grid) and Antle (draws things on grid)
drawtle = turtle.Turtle()
antle = turtle.Turtle()

# Coordinates for each square of the grid + colour (coords[x][0] = x, coords[x][1] = y, coords[x][2] = colour)

global coords
coords = []
global squaresize
squaresize = 25

# Functio to move a turtle of your choice  to a specific coordi with spped(0) and heading(0) and penup
def goooo(whichtle, x, y):
    whichtle.speed(0)
    whichtle.penup()
    whichtle.goto(x, y)
    whichtle.seth(0)
    whichtle.pendown()

def goround(whichtle, x, y):
    whichtle.speed(0)
    whichtle.penup()
    whichtle.goto(x, y)
    whichtle.pendown()
        
# Function to draw the grid with 50x50 squares  
def draw_grid():
    goooo(drawtle, -250, -250)
    drawtle.speed(0)
    drawtle.left(90)
    for i in range(int(250/squaresize)):
        coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
        print(f"Draw grid: {drawtle.position()}")
        drawtle.forward(int(squaresize))
        goround(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
        coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
        print(f"Draw grid: {drawtle.position()}")
        drawtle.right(90)
        for i in range(int(500/squaresize)):
            drawtle.forward(int(squaresize))
            goround(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
            coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
            print(f"Draw grid: {drawtle.position()}")
        drawtle.left(90)
        drawtle.forward(int(squaresize))
        goround(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
        coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
        drawtle.left(90)
        for i in range(int(500/squaresize)):
            drawtle.forward(int(squaresize))
            goround(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
            coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
            print(f"Draw grid: {drawtle.position()}")
        drawtle.right(90)

    drawtle.seth(90)
    for i in range(int(250/squaresize)):
        drawtle.right(90)
        drawtle.forward(int(squaresize))
        goround(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
        coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
        drawtle.right(90)
        for i in range(int(500/squaresize)):
            drawtle.forward(int(squaresize))
            goround(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
            coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
            print(f"Draw grid: {drawtle.position()}")
        coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
        drawtle.left(90)
        drawtle.forward(int(squaresize))
        goround(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
        coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
        drawtle.left(90)
        for i in range(int(500/squaresize)):
            drawtle.forward(int(squaresize))
            goround(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
            coords.append((drawtle.xcor(), drawtle.ycor(), "white"))
            print(f"Draw grid: {drawtle.position()}")

# Function to plot each vertex of the grid with a red dot
# This is used to check if the coordinates are correct
def coord_blot():
    drawtle.speed(0)
    for i in range(len(coords)):
        goooo(drawtle, coords[i][0], coords[i][1])
        drawtle.dot(6, "red")

# Function to fill a square with a colour and update the coordinates list
def square_fill(whichtle, colour, angle):
    whichtle.speed(0)
    whichtle.penup()
    whichtle.seth(0)
    whichtle.forward(squaresize/2)
    whichtle.left(90)
    whichtle.forward(squaresize/2)
    whichtle.right(180)
    whichtle.pendown()
    whichtle.fillcolor(colour)
    whichtle.begin_fill()
    for i in range(4):
        whichtle.forward(int(squaresize))
        whichtle.right(90)
    whichtle.end_fill()
    whichtle.penup()
    whichtle.forward(squaresize/2)
    whichtle.right(90)
    whichtle.forward(squaresize/2)
    whichtle.seth(0)
    for i in range(len(coords)):
        if int(coords[i][0]) == round(whichtle.ycor()-squaresize/2, 0) and int(coords[i][1]) == round(whichtle.xcor()-squaresize/2, 0):
            coords[i] = (coords[i][0], coords[i][1], colour)
            print(f"Filled square at {coords[i][0]}, {coords[i][1]} with {colour}, whilst turtle at {whichtle.position}")
            break
        else:
            print(f"Fill square no work: {coords[i][0], coords[i][1], whichtle.xcor(), whichtle.ycor()}")
    whichtle.seth(angle)
    
# Function to randomise the colours of the grid squares
# Can be used to randomise GoLs
def randomise_grid():
    for i in range(len(coords)):
        goooo(drawtle, coords[i][0]+squaresize/2, coords[i][1]+squaresize/2)
        colour = random.choice(["white", "black"])
        square_fill(drawtle, colour, drawtle.heading())
        coords[i] = (coords[i][0], coords[i][1], colour)


# Function to check the colour under the turtle (WHY is this not built in)
def colour_check():
    for i in range(len(coords)):
        if int(coords[i][0]) == round(antle.ycor()-squaresize/2, 0) and int(coords[i][1]) == round(antle.xcor()-squaresize/2, 0):
            return coords[i][2]
            break
        print(f"Antle checked {coords[i][0], coords[i][1]}, whilst at {antle.ycor(), antle.xcor()}")

# Function to move the turtle by a certain amount of 50x50 squares
# +dy/-dy = up/down, +dx/-dx = left/right
def coord_move(dy, dx):
    antle.penup()
    antle.seth(0)
    antle.forward(int(squaresize)*dy)
    antle.right(90)
    antle.forward(int(squaresize)*-dx)
    antle.seth(0)

# Function to draw a smiley face
def smiley():
    square_fill(antle, "black", antle.heading())
    coord_move(-3, 0)
    square_fill(antle, "black", antle.heading())
    coord_move(0, -2)
    square_fill(antle, "black", antle.heading())
    coord_move(1, -1)
    square_fill(antle, "black", antle.heading())
    coord_move(1, 0)
    square_fill(antle, "black", antle.heading())
    coord_move(1, 1)
    square_fill(antle, "black", antle.heading())

# Function to draw a heart shape
def heart():
    square_fill(antle, "red", antle.heading())
    coord_move(0, -1)
    square_fill(antle, "red", antle.heading())
    coord_move(1, 0)
    square_fill(antle, "red", antle.heading())
    coord_move(0, -1)
    square_fill(antle, "red", antle.heading())
    coord_move(1, 1)
    square_fill(antle, "red", antle.heading())
    coord_move(0, 1)
    square_fill(antle, "red", antle.heading())

def sebbycake():
    for i in range(2):
        for i in range(5):
            coord_move(1, 0)
            square_fill(antle, "burlywood1", antle.heading())
        coord_move(-5, 1)
    for i in range(5):
        coord_move(1, 0)
        square_fill(antle, "DeepPink1", antle.heading())
    coord_move(-3, 1)
    square_fill(antle, "chartreuse1", antle.heading())
    coord_move(0, 1)
    square_fill(antle, "orange", antle.heading())
    coord_move(2, -1)
    square_fill(antle, "chartreuse1", antle.heading())
    coord_move(0, 1)
    square_fill(antle, "orange", antle.heading())

    

# Function for my original purpose for this project, Langton's Ant
def the_ant():
    for i in range(1000):
        antle.speed(1)
        antle.penup()
        if colour_check() == "white":
            square_fill(antle, "black", antle.heading())
            antle.right(90)
            antle.forward(int(squaresize))
        elif colour_check() == "black":
            square_fill(antle, "white", antle.heading())
            antle.left(90)
            antle.forward(int(squaresize))
    
# Make the screen with Antle (my beloved)
s = antle.getscreen()

# Makes it so the grid is just in view
s.setup(width=500, height=500)

#Hides drawtle (the disgusting freak must be hidden)
drawtle.hideturtle()

# Move Antle to the starting position
goooo(antle, squaresize/2, squaresize/2)
s.tracer(0)
# Makes the undeserving Drawtle draw the grid
draw_grid()

# Blots the coordinates of the grid

coord_blot()
randomise_grid()
s.tracer(1)


# Uncomment the following lines to test the functions
the_ant()



#square_fill(antle, "black", antle.heading())
#square_fill(antle, "white", antle.heading())
#smiley()
#print(coords)
#coord_move(0, 6)
#heart()
#sebbycake()
print(coords)
antle.screen.exitonclick()


