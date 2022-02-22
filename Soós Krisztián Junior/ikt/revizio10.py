import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Lala = turtle.Turtle()
Lala.color("hotpink")
Lala.pensize(3)

def csillag(t,h):
    for i in range(5):
        t.penup()
        t.forward(650)
        t.right(144)
        t.pendown()
csillag(Lala, 100)
a.mainloop()