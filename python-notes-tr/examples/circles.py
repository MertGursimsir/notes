import turtle
import math

bob=turtle.Turtle()
bob.color("black")
bob.speed(10)
for i in range(2000):
	bob.fd(10)
	bob.lt(math.sin(i/10)*25)
	bob.lt(20)

turtle.done()