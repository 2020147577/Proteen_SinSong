import turtle
# set window size:
turtle.setup(800, 600)
# Set window title:
window = turtle.Screen()
window.title('Absolute Positioning')
# Get default turtle and hide:
the_turtle = turtle.getturtle()
the_turtle.hideturtle()

the_turtle.penup()
the_turtle.setposition(-400, 300)
the_turtle.pendown()  # draw line
the_turtle.setposition(400, -300)
the_turtle.penup()  # set up position
the_turtle.setposition(400, 300)
the_turtle.pendown()  # draw line
the_turtle.setposition(-400, -300)


window.exitonclick()
