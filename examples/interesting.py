import turtle
import math

bob=turtle.Turtle()
bob.color("red")
bob.speed(0)
a=0

for i in range(2000):
	bob.fd(math.sqrt(i)) 
	bob.lt(a)             #this line --> bob.lt(i%180)
	a+=1
	if a==180:
		a=0

turtle.done()