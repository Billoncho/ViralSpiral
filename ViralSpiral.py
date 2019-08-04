# ViralSpiral.py
# Billy Ridgeway
# Demostrates nested loops by creating a spiral of spirals.

import turtle               # Imports the turtle library.
t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Sets the pen's speed to fast.
t.width(2)                  # Sets the pen's width to 2.
t.penup()                   # Stops drawing.
turtle.bgcolor("black")     # Sets the background color to black.

# Ask the useer for the number of sides, default to 4, min 2 and max 6.
sides = int(turtle.numinput("Number of sides",
                         "How many sides in your spiral of spirals? (2-6)", 4, 2, 6))

# Creates a list of colors for the program.
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Our outter spiral loop.
for m in range(100):            # Set the range of m to 100.
    t.forward(m*4)              # Moves the pen forward the value of m times 4.
    position = t.position()     # Remember this corner of the spiral.
    heading = t.heading()       # Remember the direction we were heading.
    print(position, heading)    # Prints the x and y cordinates and the heading of the pen.

    # Our inner spiral loop.
    # Draws a little spiral at each corner of the big spiral.
    for n in range(int(m/2)):           # Set the range of n to the value of m divided by 2.
          t.pendown()                   # Begin drawing.
          t.pencolor(colors[n%sides])   # Cycles through the pen's colors.
          t.forward(2*n)                # Moves the pen forward 2 times the value of n.
          t.right(360/sides - 2)        # Moves the pen right the value of 360 divided by the number of sides minus 2.
          t.penup()                     # Stops drawing.
    t.setpos(position)          # Go back to the big spiral's x location.
    t.setheading(heading)       # Point in the big spiral's heading.
    t.left(360/sides + 2)       # Aim at the next point on the big spiral.
