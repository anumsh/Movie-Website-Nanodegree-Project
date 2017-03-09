import turtle

def example():
    window=turtle.Screen()
    window.bgcolor("pink")
    abc=turtle.Turtle()
    abc.speed(1)
    abc.pen(fillcolor="black", pencolor="orange", pensize=4)
    abc.stamp()
    #for alphabet R
    #abc.pu()
    abc.setpos(-55,0)
    abc.pd()
    abc.left(90)
    abc.forward(100)
    abc.right(90)
    abc.seth(90)
    abc.circle(50,180)
    abc.left(90)
    abc.forward(100)
    abc.setpos(0,0)
    
example()
