import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Sanyi= turtle.Turtle()
Sanyi.color("blue")
Sanyi.pensize(3)

def haz(t, h):
    for i in range(3):
        t.forward(50)
        t.left(120)
    t.right(90)
    for i in range(4):
        t.forward(50)
        t.left(90)

haz(Sanyi, 40)
a.mainloop()



