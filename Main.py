import turtle
import random
import time
# Drawtle 
drawtle = turtle.Turtle()


# Coordinates for each square of the grid + colour (coords[x][0] = x, coords[x][1] = y, coords[x][2] = colour)

global coords
coords = []
global squaresize
gridsidelength = 500  # Length of one side of the grid
squareamount = 22  # Number of squares along one side of the grid. Must be integer
squaresize = gridsidelength / squareamount  # Size of each square
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] # A colour scheme to be used in coord_blot.


# Functio to move a turtle of your choice  to a specific coordi with spped(0) and heading(0) and penup
def goooo(whichtle, x, y):
    whichtle.speed(0)
    whichtle.penup()
    whichtle.goto(x, y)
    whichtle.seth(0)
    whichtle.pendown()

def gohead(whichtle, x, y):
    whichtle.speed(0)
    whichtle.penup()
    whichtle.goto(x, y)
    whichtle.pendown()

def goround(whichtle):
    gohead(whichtle, round(whichtle.xcor(), 10)+1, round(whichtle.ycor(), 10)+1)

def goroundminus(whichtle):
    gohead(whichtle, round(whichtle.xcor(), 10)-1, round(whichtle.ycor(), 10)-1) 

def draw_grid(squaresize, squareamount, gridsidelength):
    #priming drawtle
    goooo(drawtle, -(gridsidelength/2), -(gridsidelength/2))
    drawtle.speed(0)
    #Draw x lines
    for i in range(squareamount+1):
        #Loop a draw to record each section of square
        for x in range(squareamount):
            print(f"Draw grid: {drawtle.position()}")
            drawtle.forward(squaresize)
            gohead(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
        goooo(drawtle, -(gridsidelength/2), (-(gridsidelength/2) + ((squaresize*(i+1)))))
    goooo(drawtle, -(gridsidelength/2), -(gridsidelength/2))
    drawtle.seth(90)
    for i in range(squareamount+1):
        #Loop a draw to record each section of square
        for x in range(squareamount):
            coords.append((round(drawtle.xcor(), 10), round(drawtle.ycor(), 10), "white"))
            print(f"Draw grid: {drawtle.position()}")
            drawtle.forward(squaresize)
            gohead(drawtle, round(drawtle.xcor(), 10), round(drawtle.ycor(), 10))
        gohead(drawtle, (-(gridsidelength/2) + ((squaresize*(i+1)))), -(gridsidelength/2))    

#Remove coord dupes from bad coding
def clean_coords(coords):
    cleaned_coords = []
    for coord in coords:
        if coord not in cleaned_coords:
            cleaned_coords.append(coord)
    return cleaned_coords

# Function to plot each vertex of the grid with a red dot
# This is used to check if the coordinates are correct
def coord_blot(coords, size, colourscheme):
    drawtle.speed(0)
    #is the colour just a colour or multile colours? - this is code fo single colour
    if type(colourscheme) == str:
        for i in range(len(coords)):
            goooo(drawtle, coords[i][0], coords[i][1])
            drawtle.dot(size, colourscheme)
    #This is code for multiple colours
    elif type(colourscheme) == list or type(colourscheme) == tuple:
        for i in range(len(coords)):
            goooo(drawtle, coords[i][0], coords[i][1])
            drawtle.dot(size, colourscheme[i % len(colourscheme)])

def coord_detect(coords, whichtle):
    for i in range(len(coords)):
        if whichtle.xcor()+0.000000001 >= coords[i][0] and whichtle.ycor()+0.000000001 >= coords[i][1]:
            if whichtle.xcor() <= coords[i][0] + squaresize-0.0000000001 and whichtle.ycor() <= coords[i][1] + squaresize-0.0000000001: # -0.0000000001 is to account for floating point errors. (I HATEH THEM I HATE THEM I HATE THEM. IT'S 01:33 AND I WAS SO DISSAPOINTED WITH MYSELF UNTIL I REALISED IT WAS ACTUALLY THE CODES FAULT THIS TIME)
                print(f"{whichtle} is in square {coords[i][0]}, {coords[i][1]}")
                return coords[i]
    print(f"{whichtle} is not in any square at {whichtle.xcor(), whichtle.ycor()}")
    return "error"
# Function to fill a square with a colour and update the coordinates list
def square_fill(whichtle, angle, squaresize, colour):
    global coords
    # Saving current coords and generic coords
    temp_coords = (whichtle.xcor(), whichtle.ycor())
    generic_coords = coord_detect(coords, whichtle)
    # Priming whichtle
    whichtle.speed(0)
    whichtle.penup()
    whichtle.seth(0)
    # Move whichtle to coord corner of square
    goooo(whichtle, generic_coords[0], generic_coords[1])
    # Filling square
    whichtle.pendown()
    whichtle.fillcolor(colour)
    whichtle.begin_fill()
    for i in range(4):
        whichtle.forward(squaresize)
        whichtle.left(90)
    whichtle.end_fill()
    print(f"Filled square {generic_coords[0]}, {generic_coords[1]} with {colour}")
    #Moving back to original coords
    goooo(whichtle, temp_coords[0], temp_coords[1])
    # Updating coords list
    coords[coords.index(generic_coords)] = (generic_coords[0], generic_coords[1], colour)
    whichtle.seth(angle)
    whichtle.penup()


# Function to randomise the colours of the grid squares
# Can be used to randomise GoLs
def randomise_grid(squaresize):
    # Loops the amount of times htere are squares. Figures this out by squaring the amount of squares on each side of the grid
    for i in range(squareamount * squareamount):
        #Goes to the corods of current square
        goooo(drawtle, coords[i][0]+0.1, coords[i][1]+0.1)  # +0.1 is to account for floating point errors
        #Chooses random colour from white or black
        colour = random.choice(["white", "black"])
        #Fills square with black if chosen
        if colour == "black":
            square_fill(drawtle, drawtle.heading(), squaresize, colour)
        #Updates coords list with new colour
        coords[i] = (coords[i][0], coords[i][1], colour)

# Function to check the colour under the turtle (WHY is this not built in)
def colour_check(whichtle):
    # Generates generic coords based on whichtle's position
    generic_coords = coord_detect(coords, whichtle)
    # Prints the generic coords, colour of coords and whichtle's position
    print(f"Whichtle checked that {generic_coords[0], generic_coords[1]} is {generic_coords[2]}, whilst at {whichtle.ycor(), whichtle.xcor()}")
    # Returns the colour of the coords
    return generic_coords[2]

# Function to move the turtle by a certain amount of squares
# +dy/-dy = up/down, +dx/-dx = left/right
def coord_move(whichtle, dx, dy, squaresize, angle=0):
    whichtle.penup()
    whichtle.seth(0)
    whichtle.forward((squaresize*dx)+0.0000000001) # +0.0000000001 is to account for floating point errors
    goooo(whichtle, round(whichtle.xcor(), 10), round(whichtle.ycor(), 10))
    whichtle.left(90)
    whichtle.forward((squaresize*dy)+0.0000000001) # +0.0000000001 is to account for floating point errors
    goooo(whichtle, round(whichtle.xcor(), 10), round(whichtle.ycor(), 10))
    whichtle.seth(angle)

# A function to draw a simple smiley face. This uses the coord_move and square_fill functions to position the turtle and aply colour.
def smiley(whichtle, squaresize):
    square_fill(whichtle, whichtle.heading(), squaresize, "black")
    coord_move(whichtle, 0, -3, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "black")
    coord_move(whichtle, -1, -1, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "black")
    coord_move(whichtle, -1, 0, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "black")
    coord_move(whichtle, -1, 1, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "black")
    coord_move(whichtle, 0, 2, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "black")

# Function to draw a heart shape. I made this for my AWESOME, BEAUTIFUL AND ABSOLUTELY GORGEOUS girlfriend, who makes my head all spinny from her effortless beauty. She said it was very cute and gave me a kiss - let's go.
def heart(whichtle, squaresize):
    square_fill(whichtle, whichtle.heading(), squaresize, "red")
    coord_move(whichtle, 0, -1, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "red")
    coord_move(whichtle, 1, 0, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "red")
    coord_move(whichtle, 0, -1, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "red")
    coord_move(whichtle, 1, 1, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "red")
    coord_move(whichtle, 0, 1, squaresize)
    square_fill(whichtle, whichtle.heading(), squaresize, "red")
    
#This is a function to draw a cake with candles on it. The formula for sections of cake is from candles is: sections of cake = (candles * 2) + 1
def agecake(whichtle, squaresize, age):
    #add a new candle with two sections of cake underneath for each year of age
    #Adding one section of cake for good looks
    # The icing of the cake
    square_fill(whichtle, whichtle.heading(), squaresize, "DeepPink1")
    #The cake base
    for x in range(2):
        coord_move(whichtle, 0, -1, squaresize)
        square_fill(whichtle, whichtle.heading(), squaresize, "burlywood1")
    coord_move(whichtle, 1, 4, squaresize)
    for i in range(age):
        #The flame of the candle
        square_fill(whichtle, whichtle.heading(), squaresize, "orange")
        coord_move(whichtle, 0, -1, squaresize)
        #The wax of the candle
        square_fill(whichtle, whichtle.heading(), squaresize, "chartreuse1")
        coord_move(whichtle, 0, -1, squaresize)
        #The two sections of cake underneath the candle
        for x in range(2):
            #The icing of the cake
            square_fill(whichtle, whichtle.heading(), squaresize, "DeepPink1")
            #The cake base
            for x in range(2):
                coord_move(whichtle, 0, -1, squaresize)
                square_fill(whichtle, whichtle.heading(), squaresize, "burlywood1")
            coord_move(whichtle, 1, 2, squaresize)
        coord_move(whichtle, 0, 2, squaresize)
def movetocentre(whichtle, squaresize, angle=0):
    goooo(whichtle, coord_detect(coords, whichtle)[0], coord_detect(coords, whichtle)[1])
    whichtle.seth(0)
    whichtle.speed(0)
    whichtle.penup()
    whichtle.forward(squaresize/2)  # Move to the middle of the square
    whichtle.right(90)
    whichtle.forward(squaresize/2)  # Move to the middle of the square
    whichtle.seth(angle)  # Set the heading to the specified angle

# Function for my original purpose for this project, Langton's Ant. The turtle will move around the grid, if it encouters a white square, it will turn right and fill the square with black. If it encounters a black square, it will turn left and fill the square with white. It will continue this process until it has moved life times.
def the_ant2(squaresize, whichtle, life):
    for i in range(life):
        goround(whichtle)
        whichtle.speed(1)
        whichtle.penup()
        if colour_check(whichtle) == "white":
            square_fill(whichtle, whichtle.heading(), squaresize, "black")
            whichtle.right(90)
            whichtle.forward(squaresize)
        else:
            square_fill(whichtle, whichtle.heading(), squaresize, "white")
            whichtle.left(90)
            whichtle.forward(squaresize)
        goroundminus(whichtle)

def startmenu():
    global gridsidelength
    global squareamount
    global squaresize
    print("Welcome to Angstroms Turtle!")
    time.sleep(0.175)
    while True:
        print("Which combination of grid side length, row square amount and square size would you like to use?")
        time.sleep(0.175)
        print("[1] Side length/Row square amount")
        time.sleep(0.175)
        print("[2] Side length/Square size")
        time.sleep(0.175)
        print("[3] Row square amount/Square size")
        inputprompt = input()
        if inputprompt == "1":
            time.sleep(0.175)
            print("Side length:\n")
            gridsidelength = int(input())
            time.sleep(0.175)
            print("Row square amount:\n")
            squareamount = int(input())
            squaresize = gridsidelength / squareamount
            break
        elif inputprompt == "2":
            time.sleep(0.175)
            print("Side length:\n")
            gridsidelength = int(input())
            time.sleep(0.175)
            print("Square size:\n")
            squaresize = int(input())
            squareamount = gridsidelength / squaresize
            break
        elif inputprompt == "3":
            time.sleep(0.175)
            print("Row square amount:\n")
            squareamount = int(input())
            time.sleep(0.175)
            print("Square size:\n")
            squaresize = int(input())
            gridsidelength = squaresize * squareamount
            break
        else:
            time.sleep(0.175)
            print("Oops! This doesn't seem to be a valid option. Please try again.")
            time.sleep(0.175)
#------------------------------------------------------------------------------------
#setting up the screen
s = drawtle.getscreen() # Makes the screen
s.setup(width=gridsidelength+10, height=gridsidelength+10) # Makes the screen the erfect size for the grid
s.title("Angstroms Turtle") # Sets the title of the screen
#------------------------------------------------------------------------------------
#Drawing things on screen
s.tracer(0) # Turn off screen updates for faster drawing
startmenu()
draw_grid(squaresize, squareamount, gridsidelength)  #Draw the grid
#                                                     Squaresize is the size of each square
#                                                     Squareamount is the number of squares along one side of the grid
#                                                     Gridsidelength is the length of one side of the grid
#                                                     Changing these in this funciton call will break the code. If you wish to change these, change the value of their variables at the top of the code.
coords = clean_coords(coords) # Remove dupe coords from the coords list from bad coding
coord_blot(coords, squaresize/6, rainbow) #Coords is the coords of the system (changing will break)
#                                          Rainbow is a list of colours of the rainbow. This can be changed to a string for single colours or a list or tuple for multiple colours.
#                                          squaresize/6 is the size of the dot. This specific value scales the size of the dot with the size of the square. This can be changed to match preferences.
s.tracer(1)  # Turn on screen updates after drawing the grid, cleaning coords and blotting the coords
#------------------------------------------------------------------------------------
#randomise_grid(squaresize)  # Randomise the grid with random colours
#                             Squaresize is the size of each square
#                             Changing this in this funciton call will break the code. If you wish to change this, change the value of its variable at the top of the code.
goooo(drawtle, 0, 0) # An alternative to the goto function. This makes sure the turtle is not dawing whilst moving and changes its rotation to be looking directly right.
#                      Drawtle is the turtle to move.
#                      0, 0 are the coords to move to. This can be changed to any coords.
coord_detect(coords, drawtle)  # A function for detecting which square the turtle is in. Is really useful in the "square_fill" function, as it allows us to find which coord in the coord list to alter the colour of.
#                                Coords is the coords of the system (changing will break).
#                                Drawtle is the turtle to check the coords of.
#square_fill(drawtle, 180, squaresize, "red") # A function that allows you to fill a square with a colour and update it on the coords list.
#                                              Drawtle is the turtle to fill the square with.
#                                              squaresize allows you to pass the size of the squares in the grid (changing this will break)
#                                              180 is the angle the turtle will end up at after fillign hte square. 180 will be left, based on the turtle roation system. This areguement was put in so that I could provide turtle.heading() to keep the turtle at the same rotation. This can be changed to anything.
#                                              "red" is the colour to fill the square with. This can be changed to anything.
print(coords) # Prints the coords list to the console. This is useful for debugging.
colour_check(drawtle)  # A function that checks the colour of the square the turtle is in and prints it to the console/returns it.
#                      Drawtle is the turtle to check the colour of.
coord_move(drawtle, -5, 0, squaresize)  # A function that moves the turtle by a certain amount of squares. This is useful for drawing with the turtle, as it allowsyou to move the turtle based on the grid system, rather than the turtle position system. For example, instead of doing "drawtle.goto(237.454545, 123.454545)", you can do "coord_move(drawtle, 4, 17, squaresize)".
#                                         Drawtle is the turtle to move.
#                                         -5 is the amount of squares to move on the x axis (this means horizontally).
#                                         0 is the amount os squares to move on the y axis (this means vertically).
#                                         squaresize is the size of the squares in the grid. This is used to calculate the distance to move the turtle.
#                                         Changing these in this funciton call will break the code. If you wish to change these, change the value of their variables at the top of the code.
#------------------------------------------------------------------------------------
smiley(drawtle, squaresize)  # A function that draws a simple smiley face. This is a fun little example of how you can use the coord_move and square_fill functions to draw pixel art.
#                              Drawtle is the turtle to draw the smiley face with.
#                              squaresize is the size of the squares in the grid. This is used to calculate the size of the smiley face.
#                              Changing this in this funciton call will break the code. If you wish to change this, change the value of its variable at the top of the code.
coord_move(drawtle, 0, 5, squaresize)  # Move the turtle up by 5 squares to make space for the next drawing.
heart(drawtle, squaresize)  # A function that draws a heart shape. This is a fun little example of how you can use the coord_move and square_fill functions to draw pixel art.
#                             Drawtle is the turtle to draw the heart shape with.
#                             squaresize is the size of the squares in the grid. This is used to calculate the size of the heart shape.
#                             Changing this in this funciton call will break the code. If you wish to change this, change the value of its variable at the top of the code.
#coord_move(drawtle, 6, 0, squaresize)  # Move the turtle right by 6 squares to make space for the next drawing.
#agecake(drawtle, squaresize, 2)  # A function that draws a cake. This is a fun little example of how you can use the coord_move and square_fill functions to draw pixel art.
#                      Drawtle is the turtle to draw the cake with.
#                      squaresize is the size of the squares in the grid. This is used to calculate the size of the cake.
#                      Changing this in this funciton call will break the code. If you wish to change this, change the value of its variable at the top of the code.
#                      2 is that age of the cake. This is a neat little feature that allows you to change the number of candles on the cake. For each 1px candle, 2 sections of cake will be drawn underneath except at the start, where one section of cake is drawn before any candles to make the cake even.
#------------------------------------------------------------------------------------
#the_ant2(squaresize, drawtle, 1000)  


drawtle.screen.exitonclick() # This stops it from throwing an error EVERYTIME I stop the program before it finishes running.