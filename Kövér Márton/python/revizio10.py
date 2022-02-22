import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Lala = turtle.Turtle()
Lala.color("hotpink")
Lala.pensize(3)

def csillag(t, h):
    for i in range(5):
        t.forward(100)
        t.right(144)
for i in range(4):
    csillag(Lala, 650)
a.mainloop()