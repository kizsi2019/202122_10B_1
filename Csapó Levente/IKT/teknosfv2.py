import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Lala= turtle.Turtle()
Lala.color("blue")
Lala.pensize(3)
def haz(t,h):
    for i in range(4):
        t.forward(h)
        t.left(90)
    t.penup()
    t.left(90)
    t.forward(h)
    t.left(90)
    t.pendown()
    for i in range(3):
        t.right(120)
        t.forward(h)
haz(Lala,100)
a.mainloop()




