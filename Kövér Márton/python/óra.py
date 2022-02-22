import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.shape("turtle")
Eszti.color("blue")

Eszti.stamp()
for i in range(12):    
    Eszti.penup()
    Eszti.forward(120)
    Eszti.pendown()
    Eszti.forward(20)
    Eszti.penup()
    Eszti.forward(20)
    Eszti.stamp()
    Eszti.backward(160)
    Eszti.left(30)
ablak.mainloop()