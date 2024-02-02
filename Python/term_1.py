import turtle
wn=turtle.Screen().bgcolor("black")
color = ['red','purple','blue','green','orange']
t=turtle.Turtle()
t.speed(18)
for x in range(250):
    t.pencolor(color[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)