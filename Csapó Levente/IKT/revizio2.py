import turtle
a = turtle.Screen()
a.bgcolor("black")
Lala= turtle.Turtle()
Lala.color("white")
Lala.pensize(3)

def negyzet_valami(t,h):
    meret = h
    for i in range(4):
        t.forward(meret)
        t.left(90)
        
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()
    
h = 20
for i in range(5):
    negyzet_valami(Lala, h)
    h = h + 20
    
a.mainloop()
