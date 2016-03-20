__author__ = 'premaseem'

import turtle

def draw():
    print "drawing started"
    window = turtle.Screen()
    window.bgcolor("red")
    shampy2 = turtle.Turtle()
    shampy2.shape("turtle")
    shampy2.speed(1)
    shampy2.color("yellow")
    shampy2.forward(100)
    shampy2.right(60)
    shampy2.forward(100)
    shampy2.right(60)
    shampy2.forward(100)
    shampy2.right(60)
    shampy2.forward(100)



    shampy = turtle.Turtle()
    shampy.shape("turtle")
    shampy.speed(3)
    shampy.color("yellow")
    shampy.forward(100)
    shampy.right(90)
    shampy.forward(100)
    shampy.right(90)
    shampy.forward(100)
    shampy.right(90)
    shampy.forward(100)



    shampy1 = turtle.Turtle()
    shampy1.shape("turtle")
    shampy1.speed(5)
    shampy1.color("orange")
    shampy1.forward(200)
    shampy1.right(90)
    shampy1.forward(200)
    shampy1.right(90)
    shampy1.forward(200)
    shampy1.right(90)
    shampy1.forward(200)

    boobs = turtle.Turtle()
    boobs.shape("circle")
    boobs.circle(100)
    window.exitonclick()


draw()


