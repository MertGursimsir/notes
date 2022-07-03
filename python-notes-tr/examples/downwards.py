import turtle

pen=turtle.Turtle()
pen.color("#4A60CD", "red")
pen.width(10)
pen.speed(1)

pen.begin_fill()
pen.fd(100)
pen.rt(120)
pen.fd(100)
pen.rt(120)
pen.fd(100)


pen.penup()
pen.rt(210)
pen.forward(100)
pen.pendown()

pen.lt(90)
pen.fd(100)
pen.rt(120)
pen.fd(100)
pen.rt(120)
pen.fd(100)
pen.end_fill()


turtle.done()