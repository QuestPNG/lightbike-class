import turtle
import time

screen = turtle.Screen()
screen.tracer(0)

# Bike 1
bike1 = turtle.Turtle()
bike1.goto(0, -50)
r = 0.5
g = 0.2
b = 0.3
bike1.color(r, g, b)

# Bike 2
bike2 = turtle.Turtle()
bike2.color("magenta")


def bike1left():
    bike1.left(90)


def bike1right():
    bike1.right(90)


def updateColors():
    global r
    global b
    global g
    r += 0.1
    b += 0.2
    g += 0.3

    if r > 1:
        r = 0
    if g > 1:
        g = 0
    if b > 1:
        b = 0


screen.onkeypress(bike1left, "Left")
screen.onkeypress(bike1right, "Right")
screen.listen()

# checkEdges()
# screen.window_width
#if bike1.pos()[0] > screen.window_width()/2:
#bike1.goto(-screen.window_width()/2, bike1.pos()[1])


while True:
    bike1.forward(1)
    updateColors()
    bike1.color(r, g, b)
    screen.update()
    time.sleep(0.05)
