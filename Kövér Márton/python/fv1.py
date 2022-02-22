import turtle

def negyzet_rajzolas(t, h):
    """Egy h oldalhosszúságú négyzet rajzolása a teknoccel"""
    for i in range(4):
        t.forward(h)
        t.left(120)
a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("Sanyi találkozik egy függvénnyel")

Sanyi = turtle.Turtle()
negyzet_rajzolas(Sanyi, 50)
a.mainloop()