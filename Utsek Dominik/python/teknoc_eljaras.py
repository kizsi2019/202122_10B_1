import turtle

def negyzet_rajzolas(t,h):
    for i in range(8):
        t.forward(h)
        t.left(60)
a =turtle.Screen()
a.bgcolor("lightgreen")
a.title ("Sanyi találkozik a fügvénnyel")

Sanyi =turtle.Turtle()

negyzet_rajzolas(Sanyi, 50)
a.mainloop()

