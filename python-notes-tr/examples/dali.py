import turtle
my_turtle=turtle.Turtle()
my_turtle.color("red", "yellow")
my_turtle.speed(0)


my_turtle.begin_fill()
for i in range(100):
    my_turtle.forward(i**2)
    my_turtle.left(170)


my_turtle.end_fill()

turtle.done()