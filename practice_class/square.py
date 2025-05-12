import turtle

# set window size:
turtle.setup(800, 600)

# get reference to turtle window:
window = turtle.Screen()

# set window title bar:
window.title('My First Turtle Graphics Program')

the_turtle = turtle.getturtle()
the_turtle.hideturtle()

the_turtle.setposition(100, 0)
the_turtle.setposition(100, 100)
the_turtle.setposition(0, 100)
the_turtle.setposition(0, 0)

window.exitonclick()
