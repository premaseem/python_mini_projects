__author__ = 'asee2278'
import turtle



def draw_sqaure(shape):
    for i,j in enumerate(range(4)):
        shape.forward(150)
        shape.right(90)



def draw():
    print "drawing started"
    window = turtle.Screen()
    window.bgcolor("red")

    shampy = turtle.Turtle()
    shampy.shape("turtle")
    shampy.speed(9)
    shampy.color("yellow")
    for x in range(1,37):
        draw_sqaure(shampy)
        shampy.right(10)

    window.exitonclick()

draw()


