import turtle

def negyzet_rajzolas(t,h):
    for i in range(4):
        t.forward(h)
        t.left(120)
a = turtle.Screen()
a.bgcolor("lightgreen")

a.title("Sanyi találkozok a fügvénnyel")

sanyi = turtle.Turtle()
negyzet_rajzolas(sanyi, 50)
a.mainloop()