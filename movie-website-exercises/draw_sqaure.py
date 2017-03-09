
import turtle #module

def draw_square():
    window=turtle.Screen()
    window.bgcolor("green")
    
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.speed(2)

    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

draw_square()



"""
import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("pink")
    brad=turtle.Turtle()
    brad.shape("triangle")
    brad.speed("normal")
    brad.color("blue")
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

draw_square()
"""
