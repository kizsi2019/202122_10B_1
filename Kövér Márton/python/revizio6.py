import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Lala = turtle.Turtle()
Lala.color("blue")
Lala.pensize(2)
def spiral(t, h):
    hossz = h
    for i in range(92):
        t.forward(hossz)
        hossz = hossz + 3
        t.right(89)

spiral(Lala, 3)
a.mainloop()