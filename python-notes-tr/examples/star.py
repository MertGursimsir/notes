import turtle

bob=turtle.Turtle()
bob.color("red", "yellow")
bob.speed(10)


bob.begin_fill()
for i in range(100):
	bob.fd(300)
	bob.lt(170 )
	if abs(bob.pos())<1:
		break
bob.end_fill( )

turtle.done()