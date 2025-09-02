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
# Some example colour schemes
colour_schemes = {
    "Rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    "Grayscale": ["black", "gray50", "gray", "gray20", "gray80", "gainsboro", "white"],
    "Warm": ["red", "orange", "yellow", "gold", "DarkOrange", "tomato"],
    "Cool": ["blue", "cyan", "teal", "navy", "purple", "indigo"],
    "Nature": ["ForestGreen", "SaddleBrown", "OliveDrab", "DarkGoldenrod", "SeaGreen"],
    "Ocean": ["DeepSkyBlue", "DodgerBlue", "MediumBlue", "navy", "teal"],
    "Sunset": ["OrangeRed", "DarkOrange", "goldenrod", "gold", "LightYellow"],
    "Pastel": ["LightPink", "LightBlue", "LightGreen", "lavender", "PeachPuff"],
    "Trans": ["cyan", "LightPink2", "white", "LightPink2", "cyan"],
    "Nonbinary": ["yellow", "white", "purple", "black"],
    # Add more colour schemes as needed
}

# List to keep track of all ants
ant_list = {
    "Drawtle": drawtle,
    # Add more ants here as needed
}

preset_drawings = {
    "Smiley": ["black", (0, -3), "black", (-1, -1), "black", (-1, 0), "black", (-1, 1), "black", (0, 3), "black"],
    "Heart": ["red", (0, -1), "red", (1, 0), "red", (0, -1), "red", (1, 1), "red", (0, 1), "red"],
}

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
    whichtle.penup()

def goroundminus(whichtle):
    gohead(whichtle, round(whichtle.xcor(), 10)-1, round(whichtle.ycor(), 10)-1) 
    whichtle.penup()
    

def draw_grid(squaresize, squareamount, gridsidelength, whichtle=drawtle):
    #priming whichtle
    goooo(whichtle, -(gridsidelength/2), -(gridsidelength/2))
    whichtle.speed(0)
    #Draw x lines
    for i in range(squareamount+1):
        #Loop a draw to record each section of square
        for x in range(squareamount):
            print(f"Draw grid: {whichtle.position()}")
            whichtle.forward(squaresize)
            gohead(whichtle, round(whichtle.xcor(), 10), round(whichtle.ycor(), 10))
        goooo(whichtle, -(gridsidelength/2), (-(gridsidelength/2) + ((squaresize*(i+1)))))
    goooo(whichtle, -(gridsidelength/2), -(gridsidelength/2))
    whichtle.seth(90)
    for i in range(squareamount+1):
        #Loop a draw to record each section of square
        for x in range(squareamount):
            coords.append((round(whichtle.xcor(), 10), round(whichtle.ycor(), 10), "white"))
            print(f"Draw grid: {whichtle.position()}")
            whichtle.forward(squaresize)
            gohead(whichtle, round(whichtle.xcor(), 10), round(whichtle.ycor(), 10))
        gohead(whichtle, (-(gridsidelength/2) + ((squaresize*(i+1)))), -(gridsidelength/2))    

#Remove coord dupes from bad coding
def clean_coords(coords):
    global squareamount
    cleaned_coords = []
    for coord in coords:
        if coord not in cleaned_coords:
            cleaned_coords.append(coord)
    for i in range(squareamount-1):
        cleaned_coords.pop()
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
""" def coord_detect2(coords, whichtle):
    global squaresize
    xcor = whichtle.xcor()+0.000000001 # +0.0000000001 is to account for rounding errors
    ycor = whichtle.ycor()+0.000000001
    for i in range(len(coords)):
        if(coords[i][0] - xcor <= squaresize and coords[i][0] - xcor >= 0):
            if(coords[i][1] - ycor <= squaresize and coords[i][1] - ycor >= 0):
                print(f"{whichtle} is in square {coords[i][0]}, {coords[i][1]}")
                return coords[i] """
def coord_detect2(coords, whichtle):
    global squaresize
    xcor = whichtle.xcor()+0.00000001 # +0.0000000001 is to account for rounding errors
    ycor = whichtle.ycor()+0.00000001
    results = []
    for i in range(len(coords)):
        if(xcor - coords[i][0] < squaresize and xcor - coords[i][0] >= -squaresize):
            if(ycor - coords[i][1] < squaresize and ycor - coords[i][1] >= -squaresize):
                results.append([coords[i], xcor - coords[i][0]])
                if len(results) == 2:
                    print(f"{whichtle} is in  square {min(results)[0]}, {min(results)[1]}")
                    return min(results)


# FIX COORD DETECT 2

# Function to fill a square with a colour and update the coordinates list
def square_fill(whichtle, angle, squaresize, colour):
    global coords
    s.tracer(0)
    # Saving current coords and generic coords
    temp_coords = (whichtle.xcor(), whichtle.ycor())
    generic_coords = coord_detect2(coords, whichtle)
    # Priming whichtle
    whichtle.speed(0)
    whichtle.penup()
    whichtle.seth(0)
    # Move whichtle to coord corner of square
    try:
        goooo(whichtle, generic_coords[0], generic_coords[1])
    except TypeError:
        print(f"Error: {whichtle} is out of bounds at {whichtle.xcor(), whichtle.ycor()}. Cannot fill square.")
        return
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
    s.tracer(1)


# Function to randomise the colours of the grid squares
# Can be used to randomise GoLs
def randomise_grid(squaresize, whichtle=drawtle):
    global coords
    seed = []
    whichtle.speed(0)
    for i in range(len(coords)):
        seed.append(random.choice([True, False]))
    for i in range(len(seed)):
        if seed[i]:
            goooo(whichtle, coords[i][0], coords[i][1])
            goround(whichtle)
            square_fill(whichtle, whichtle.heading(), squaresize, "black")

# Function to check the colour under the turtle (WHY is this not built in)
def colour_check(whichtle):
    # Generates generic coords based on whichtle's position
    generic_coords = coord_detect2(coords, whichtle)
    # Prints the generic coords, colour of coords and whichtle's position
    print(f"Whichtle checked that {generic_coords[0], generic_coords[1]} is {generic_coords[2]}, whilst at {whichtle.ycor(), whichtle.xcor()}")
    # Returns the colour of the coords
    return generic_coords[2]

# Function to move the turtle by a certain amount of squares
# +dy/-dy = up/down, +dx/-dx = left/right
def coord_move(whichtle, dx, dy, squaresize, angle=0):
    s.tracer(1)
    whichtle.penup()
    whichtle.seth(0)
    whichtle.forward((squaresize*dx)+0.0000000001) # +0.0000000001 is to account for floating point errors
    goooo(whichtle, round(whichtle.xcor(), 10), round(whichtle.ycor(), 10))
    whichtle.penup()
    whichtle.left(90)
    whichtle.forward((squaresize*dy)+0.0000000001) # +0.0000000001 is to account for floating point errors
    goooo(whichtle, round(whichtle.xcor(), 10), round(whichtle.ycor(), 10))
    whichtle.seth(angle)

# A function to draw a simple smiley face. This uses the coord_move and square_fill functions to position the turtle and apply colour.
def preset_draw(whichtle, squaresize, drawing_name):
    whichtle.speed(0)
    print(f"{whichtle} is drawing {drawing_name}.")
    for i in range(len(preset_drawings[drawing_name])):
        if type(preset_drawings[drawing_name][i]) == str:
            square_fill(whichtle, whichtle.heading(), squaresize, preset_drawings[drawing_name][i])
        else:
            coord_move(whichtle, preset_drawings[drawing_name][i][0], preset_drawings[drawing_name][i][1], squaresize)



    
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
    goooo(whichtle, coord_detect2(coords, whichtle)[0], coord_detect2(coords, whichtle)[1])
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
        if coord_detect2(coords, whichtle)[2] == "white":
            square_fill(whichtle, whichtle.heading(), squaresize, "black")
            whichtle.right(90)
            whichtle.forward(squaresize)
        else:
            square_fill(whichtle, whichtle.heading(), squaresize, "white")
            whichtle.left(90)
            whichtle.forward(squaresize)
        goroundminus(whichtle)


def make_ant(name, ant_list=ant_list):
    ant_list[name] = turtle.Turtle()
    print(f"Made a new ant called {name}!")   

def startmenu(colour_schemes=colour_schemes, whichtle=drawtle):
    global gridsidelength
    global squareamount
    global squaresize
    global coords

    blot_option = False
    print("Welcome to Angstroms Turtle!")
    time.sleep(0.25)
    while True:
        print("Which combination of grid side length, row square amount and square size would you like to use?")
        time.sleep(0.25)
        print("[1] Side length/Row square amount")
        time.sleep(0.25)
        print("[2] Side length/Square size")
        time.sleep(0.25)
        print("[3] Row square amount/Square size")
        inputprompt = input()
        if inputprompt == "1":
            time.sleep(0.25)
            print("Side length:")
            gridsidelength = int(input())
            time.sleep(0.25)
            print("Row square amount:")
            squareamount = int(input())
            squaresize = int(gridsidelength / squareamount)
            break
        elif inputprompt == "2":
            time.sleep(0.25)
            print("Side length:")
            gridsidelength = int(input())
            time.sleep(0.25)
            print("Square size:")
            squaresize = int(input())
            squareamount = int(gridsidelength / squaresize)
            break
        elif inputprompt == "3":
            time.sleep(0.25)
            print("Row square amount:")
            squareamount = int(input())
            time.sleep(0.25)
            print("Square size:")
            squaresize = int(input())
            gridsidelength = squaresize * squareamount
            break
        else:
            time.sleep(0.25)
            print("Oops! This doesn't seem to be a valid option. Please try again.")
            time.sleep(0.25)
    while True:
        print("Would you like to blot the coordinates on the grid?")
        time.sleep(0.25)
        print("[1] Yes")
        time.sleep(0.25)
        print("[2] No")
        inputprompt = input()
        if inputprompt == "1":
            blot_option = True
            print("Which colour scheme would you like to use?")
            for i in range(len(colour_schemes)):
                time.sleep(0.5)
                print(f"[{i+1}] {list(colour_schemes.keys())[i]}")
            print(f"[{len(colour_schemes)+1}] Single Colour")
            inputprompt = input()
            if inputprompt == str(len(colour_schemes)+1):
                while True:
                    time.sleep(0.25)
                    print("Which colour would you like to use?")
                    colour = input()
                    try:
                        whichtle.color(colour)
                    except:
                        time.sleep(0.25)
                        print("Oops! This doesn't seem to be a valid colour. Please try again.")
                        time.sleep(0.25)
                    whichtle.color("black")
                    break
                break
            elif int(inputprompt) in range(1, len(colour_schemes)+1):
                colour = list(colour_schemes.values())[int(inputprompt)-1]
                break
            else:
                time.sleep(0.25)
                print("Oops! This doesn't seem to be a valid option. Please try again.")
                time.sleep(0.25)
        elif inputprompt == "2":
            break
        else:
            time.sleep(0.25)
            print("Oops! This doesn't seem to be a valid option. Please try again.")
            time.sleep(0.25)
    draw_grid(squaresize, squareamount, gridsidelength, whichtle)  #Draw the grid
#                                                     Squaresize is the size of each square
#                                                     Squareamount is the number of squares along one side of the grid
#                                                     Gridsidelength is the length of one side of the grid
#                                                     Changing these in this funciton call will break the code. If you wish to change these, change the value of their variables at the top of the code.
    coords = clean_coords(coords) # Remove dupe coords from the coords list from bad coding
    if blot_option == True:
        coord_blot(coords, squaresize/6, colour)#Coords is the coords of the system (changing will break)
#                                          Rainbow is a list of colours of the rainbow. This can be changed to a string for single colours or a list or tuple for multiple colours.
#                                          squaresize/6 is the size of the dot. This specific value scales the size of the dot with the size of the square. This can be changed to match preferences.
    s.tracer(1)
    goooo(whichtle, 0, 0)  # Move whichtle to the centre of the grid
    whichtle.seth(0)

# REMINDER: Add colour scheme option. Will need to change root function too

def randomise_grid_menu(whichtle=drawtle):
    while True:
        print("Would you like to see the proccess (this may slow down the randomisation)?")
        inputprompt = input("[1] Yes\n[2] No\n")
        if inputprompt.isnumeric():
            if int(inputprompt) == 2:
                s.tracer(0)
            if int(inputprompt) in [1, 2]:
                break
            else:
                print("Oops! This doesn't seem to be a valid option. Please try again.")
                time.sleep(0.2)
                continue
        else:
            print("Oops! This doesn't seem to be a valid option. Please try again.")
            time.sleep(0.2)
            continue
    print("Randomising grid...")
    randomise_grid(squaresize, whichtle)
    s.tracer(1)
    print("Grid randomised!")

def coord_move_menu(whichtle=drawtle):
    while True:
        print("How many squares would you like to move the ant by on the x axis (horizontally)?")
        dx = input()
        try:
            int(dx)
        except:
            print("Oops! This doesn't seem to be a valid option. Please try again.")
            time.sleep(0.2)
            continue
        print("How many squares would you like to move the ant by on the y axis (vertically)?")
        dy = input()
        try:
            int(dy) 
        except:
            print("Oops! This doesn't seem to be a valid option. Please try again.")
            time.sleep(0.2)
            continue
        break
    coord_move(whichtle, int(dx), int(dy), squaresize)
    print(f"{whichtle} moved by {[dx, dy]} squares!")

def square_fill_menu(whichtle=drawtle):
    while True:
        print("Which colour would you like to fill the square with?")
        colour = input()
        try:
            whichtle.color(colour)
            break
        except:
            print("Oops! This doesn't seem to be a valid colour. Please try again.")
            time.sleep(0.2)
            continue
    square_fill(whichtle, whichtle.heading(), squaresize, colour)
    whichtle.color("black")

def preset_drawing_menu(whichtle=drawtle):
    while True:
        print("Which preset drawing would you like to use?")
        for i in range(len(preset_drawings)):
            time.sleep(0.175)
            print(f"[{i+1}] {list(preset_drawings.keys())[i]}")
        inputprompt = input()
        if inputprompt.isnumeric():
            if int(inputprompt) in range(1, len(preset_drawings)+1):
                drawing_name = list(preset_drawings.keys())[int(inputprompt)-1]
                break
            else:
                print("Oops! This doesn't seem to be a valid option. Please try again.")
                time.sleep(0.2)
                continue
        else:
            print("Oops! This doesn't seem to be a valid option. Please try again.")
            time.sleep(0.2)
            continue
    preset_draw(whichtle, squaresize, drawing_name)

def the_ant2_menu(whichtle=drawtle):
    while True:
        print("How many cycles would you like the ant to run for?")
        inputprompt = input()
        if inputprompt.isnumeric():
            life = int(inputprompt)
            break
        else:
            print("Oops! This doesn't seem to be a valid option. Please try again.")
            time.sleep(0.2)
            continue
    the_ant2(squaresize, whichtle, life)

def make_ant_menu(placeholder, ant_list=ant_list):
    while True:
        print("What would you like to name your new ant?")
        inputprompt = input()
        if inputprompt in ant_list.keys():
            print("Oops! An ant with this name already exists. Please try again.")
            time.sleep(0.2)
            continue
        else:
            make_ant(inputprompt, ant_list)
            break
def main_menu(ant_list=ant_list):
    
    # Menu options to reduce amount of if statements in the menu code
    menu_options = {
        "1": randomise_grid_menu,
        "2": coord_move_menu,
        "3": square_fill_menu,
        "4": preset_drawing_menu,
        "5": the_ant2_menu,
        "6": make_ant_menu,
    }
    while True:
        while True:
            print("Which action would you like to perform")
            time.sleep(0.2)
            print("[1] Randomise grid")
            time.sleep(0.2)
            print("[2] Move turtle")
            time.sleep(0.2)
            print("[3] Fill square")
            time.sleep(0.2)
            print("[4] Use a preset drawing")
            time.sleep(0.2)
            print("[5] Begin Langton's Ant")
            time.sleep(0.2)
            print("[6] Make another ant")
            inputprompt = input()
            if (inputprompt.isnumeric()) != True:
                print("Oops! This doesn't seem to be a valid option. Please try again.")
                time.sleep(0.2)
                continue
            elif int(inputprompt) not in range(1, len(menu_options)+1):
                print("Oops! This doesn't seem to be a valid option. Please try again.")
                time.sleep(0.2)
                continue
            else:
                break
        while True:
            print("Which ant would you like to use?")
            for i in range(len(ant_list)):
                time.sleep(0.2)
                print(f"[{i+1}] {list(ant_list.keys())[i]}")
            inputprompt2 = input()
            if inputprompt2.isnumeric():
                if int(inputprompt2) in range(1, len(ant_list)+1):
                    whichtle = list(ant_list.values())[int(inputprompt2)-1]
                    break
                else:
                    print("Oops! This doesn't seem to be a valid option. Please try again.")
                    time.sleep(0.2)
                    continue
            else:
                print("Oops! This doesn't seem to be a valid option. Please try again.")
                time.sleep(0.2)
                continue
        menu_options[str(inputprompt)](whichtle)



#------------------------------------------------------------------------------------
#setting up the screen
s = drawtle.getscreen() # Makes the screen
s.setup(width=gridsidelength+10, height=gridsidelength+10) # Makes the screen the erfect size for the grid
s.title("Angstroms Turtle") # Sets the title of the screen
#------------------------------------------------------------------------------------
#Drawing things on screen
s.tracer(0) # Turn off screen updates for faster drawing
startmenu()
s.tracer(1)
#preset_draw(drawtle, squaresize, "Heart")
main_menu()
#------------------------------------------------------------------------------------
""" #randomise_grid(squaresize)  # Randomise the grid with random colours
#                             Squaresize is the size of each square
#                             Changing this in this funciton call will break the code. If you wish to change this, change the value of its variable at the top of the code.
s.tracer(1)  # Turn on screen updates after drawing the grid, cleaning coords and blotting the coords
drawtle.forward(10)
print(coords)
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
goround(drawtle)
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

 """
drawtle.screen.exitonclick() # This stops it from throwing an error EVERYTIME I stop the program before it finishes running.