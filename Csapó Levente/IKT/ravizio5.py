import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Lala = turtle.Turtle()
Lala.color("blue")
Lala.pensize(2)
def spiral(t,h):
    hossz = h
    for i in range(90):
        t.forward(hossz)
        hossz = hossz +2
        t.right(87)
        
spiral(Lala, 3)
a.mainloop()