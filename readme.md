# Angstrom's Turtle ![Logo](https://github.com/cap-heavenly/angstroms-turtle/blob/main/assets/angstromsturtle.jpg?raw=true)

> A grid system, art-maker and GoL framework

This project orginiated as a curious attempt to replicate the famous "Langton's Ant". Though, through an exploration of the underlying mechanisms of how the coordinate system, grid drawing and colour-checking operated, my intial intentions significantly changed.

## What does each file do?

• Main.py - This is the main file, it should be able to run by itself and if it is from the main branch, should not contain any errors. If you use it and discover and errors or unintended behaviour, please report it using github or by contacting be directly.

• LegacyMain.py - This is a version of the main file from before the full script rework, I wanted to include this in the project as it showcases the contrast in understanding of the python language and turtle module that this project has provided me relative to what I started with.

• Cleaner.py - This is a script that was used in the LegacyMain.py to create the list of coordinates as well as saturate it with white colour tags. It is also used to prototype things that have not been fully developed yet.

• assets - This is just a folder for images in the readme. It includes things like the logo that I have created for this project, which consists of the official python logo and a simplified version of one of the drones operated by "Angstrom Levy" in the show "Invincible" as that is where the "Angstrom's" part of the name comes from.
> If you haven't already, I would highly recommend watching "Invincible"

## What does it actually do?

This project has functions to execute a variety of tasks:

• draw_grid(squaresize, squareamount, gridsidelength) - This is a function which allows you to draw a grid with the provided specifications.
> NOTE: squareamount refers to the amount of squares on one row/column of the grid not the total amount of square in the grid

> NOTE: You will only need to come up with two of the specifications, then use this formula: "squaresize = gridsidelength / squareamount" to work out the third.

## *Read me will be completed when changes are finalised*
