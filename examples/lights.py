import turtle 
import time

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Stoplights")

pen=turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30,-60)
pen.pendown()
pen.fd(60)
pen.lt(90)
pen.fd(120)
pen.lt(90)
pen.fd(60)
pen.lt(90)
pen.fd(120)

red=turtle.Turtle()
red.shape("circle")
red.color("grey")
red.penup()
red.goto(0,40)

yellow=turtle.Turtle()
yellow.shape("circle")
yellow.color("grey")

green=turtle.Turtle()
green.shape("circle")
green.color("grey")
green.penup()
green.goto(0,-40)

while True:
	red.color("red")
	time.sleep(2)
	red.color("grey")

	green.color("green")
	time.sleep(2)
	green.color("grey")

	yellow.color("yellow")
	time.sleep(1)
	yellow.color("grey")

wn.mainloop()