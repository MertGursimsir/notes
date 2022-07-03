import turtle

c=["#4D1214", "#511113", "#890C10", "#A21B20","#D01D23"]

pen=turtle.Turtle()
pen.penup()
pen.goto(0,100)
pen.pendown()
pen.speed(10)
pen.getscreen().bgcolor("black")
a=0
b=98
d=150
for i in range(400):
	pen.color(c[a])
	a+=1
	if a>3:
		a=0
	pen.fd(d)
	pen.lt(b)
	d-=1

turtle.done()