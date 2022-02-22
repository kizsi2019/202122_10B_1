import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
turtle.color("hotpink")
Lala = turtle.Turtle()
Lala.pensize(3)

def csillag(t, h):
    for i in range(5):
        t.forward(h)
        t.left(144)
        t.forward(650)
csillag(Lala, 100)
a.mainloop()
