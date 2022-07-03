import turtle 

pegasus=turtle.Turtle()
pegasus.getscreen().bgcolor("#994444")

pegasus.penup()
pegasus.goto(-200,100)
pegasus.pendown()

def star(turtle, size):
	if size>10:
		turtle.speed(0)
		turtle.begin_fill()
		for i in range(5):
			turtle.fd(size)
			star(turtle, size/3)
			turtle.lt(216)
		turtle.end_fill()
	else:
		return None

star(pegasus, 360)

turtle.done()