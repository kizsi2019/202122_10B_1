import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Eszti= turtle.Turtle()
Eszti.color("blue")
Eszti.pensize(3)

def negyzet_rajzolas(t, h):
    for i in range(4):
        t.forward(h)
        t.left(90)
    t.left(360/20)
    
for i in range(20):
    negyzet_rajzolas(Eszti, 100)
        
        
a.mainloop()        