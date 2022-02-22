import turtle
def ablak_keszites(szin, ablaknev):
    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablaknev)
    return a
def teknoc_keszites(szin, tm):
    t = turtle.Turtle()
    t.color(szin)
    t.pensize(tm)
    return t
a = ablak_keszites("lightgreen", "Eszti és Sanyi táncol")
Eszti = teknoc_keszites("hotpink", 5)
Sanyi = teknoc_keszites("black", 1)
David = teknoc_keszites("yellow", 2)

Eszti.forward(20)
Sanyi.left(180)
Sanyi.forward(60)
David.left(90)
David.forward(120)

a.mainloop()