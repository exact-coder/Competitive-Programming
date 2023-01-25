import turtle
import random



turtle.Screen().bgcolor('black')
t = turtle.Turtle()

t.setpos(0,300)
t.color('Orange')
style =('Courier', 50, 'bold')
t.write('Wellcome Ramadan', font=style,align='center')
t.penup()
t.setpos(0,0)
t.pendown()

def pen(colour):
    t.color(colour)

def fireworks(distance):
    for _ in range(20):
        t.forward(distance)
        t.right(180-(360/20))

def move():
    t.penup()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    t.goto(x,y)
    t.pendown()

t.speed(0)
colors = ['red','purple','green','blue','orange','yellow','gray','navy','blueviolet','brown','chartreuse','coral','chocolate']
for i in range(50):
    color =random.choice(colors)
    pen(color)
    fireworks(random.randint(50,80))
    move()
turtle.done()