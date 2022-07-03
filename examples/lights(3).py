import turtle

wn=turtle.Screen()
wn.title("Stoplights with Classes")
wn.bgcolor("black")

class Stoplights():
	def __init__(self,x,y):
		self.pen=turtle.Turtle()
		self.pen.penup()
		self.pen.hideturtle()
		self.pen.speed(0)
		self.pen.color("red")
		self.pen.goto(x-30,y+60)
		self.pen.down()
		self.pen.fd(60)
		self.pen.rt(90)
		self.pen.fd(120)
		self.pen.rt(90)
		self.pen.fd(60)
		self.pen.rt(90)
		self.pen.fd(120)

		self.color=""

		self.red=turtle.Turtle()
		self.yellow=turtle.Turtle()
		self.green=turtle.Turtle()

		self.red.speed(0)
		self.yellow.speed(0)
		self.green.speed(0)

		self.red.color("grey")
		self.yellow.color("grey")
		self.green.color("grey")

		self.red.shape("circle")
		self.yellow.shape("circle")
		self.green.shape("circle")

		self.red.penup()
		self.yellow.penup()
		self.green.penup()

		self.red.goto(x,y+40)
		self.yellow.goto(x,y)
		self.green.goto(x,y-40)

	def change_color(self,color):

		self.red.color("grey")
		self.yellow.color("grey")
		self.green.color("grey")

		if color=="red":
			self.red.color("red")
			self.color="red"
		elif color=="yellow":
			self.yellow.color("yellow")
			self.color="yellow"
		elif color=="green":
			self.green.color("green")
			self.color="green"	
		else:
			print("Error: Unknown color {}".format(color))	

	def timer(self):
		if self.color=="red":
			self.change_color("green")
			wn.ontimer(self.timer, 2000)
		elif self.color=="yellow":
			self.change_color("red")
			wn.ontimer(self.timer, 2000)
		elif self.color=="green":
			self.change_color("yellow")
			wn.ontimer(self.timer, 2000)


			
stoplight=Stoplights(0,0)
stoplight.change_color("red")
stoplight.timer()

stoplight2=Stoplights(-100,0)
stoplight2.change_color("yellow")
stoplight2.timer()

stoplight3=Stoplights(100,0)
stoplight3.change_color("green")
stoplight3.timer()

wn.mainloop() 