import turtle
Sanyi = turtle.Turtle()
a = turtle.Screen()
a.bgcolor("lightgreen")
Sanyi.color("hotpink")
Sanyi.pensize(2)
def negyzet(t,h):
    for i in range(4):
        t.forward(h)
        t.left(90)
    t.penup()
    t.forward(2*h)
    t.pendown()
for i in range(5):
    negyzet(Sanyi,50)

a.mainloop()
