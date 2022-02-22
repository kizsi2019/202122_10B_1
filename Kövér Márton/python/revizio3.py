import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.color("hotpink")
Eszti.pensize(3)

def sokszog_rajzolas(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
sokszog_rajzolas(Eszti, 360, 1)

a.mainloop()