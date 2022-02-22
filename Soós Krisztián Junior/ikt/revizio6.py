import turtle
a = turtle.Screen()
Lala = turtle.Turtle()
Lala.pensize(3)

def csillag(t,h):
    for i in range(5):
        t.forward(h)
        t.right(144)
        
csillag(Lala, 100)
a.mainloop()