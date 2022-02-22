import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Sanyi= turtle.Turtle()
Sanyi.color("hotpink")
Sanyi.pensize(3)

def negyzet_valami(t, h):
    for i in range(4):
        t.forward(h)
        t.left(90)
    t.penup()
    t.forward(2*h)
    t.pendown()

for i in range(5):
    negyzet_valami(Sanyi, 20)
a.mainloop()