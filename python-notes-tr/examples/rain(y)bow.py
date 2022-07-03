import turtle 

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Ahsen")

c=["red", "yellow", "cyan", "blue","green"]

a=0
x=100
y=60
pen=turtle.Turtle()
pen.speed(0)
for i in range(100):
	pen.color(c[a])
	a+=1
	if a>4:
		a=0
	pen.fd(x)
	pen.rt(y)
	x-=5


wn.mainloop()