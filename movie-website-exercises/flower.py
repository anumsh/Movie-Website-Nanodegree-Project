import turtle

window = turtle.Screen()
window.bgcolor("pink")

abc =turtle.Turtle()
abc.shape("arrow")
abc.color("red","green")
abc.pensize(4)
abc.stamp()
abc.shape("classic")
abc.color("blue")
abc.speed(1)

#abc.pu()
#abc.setpos(-200,0)
#abc.pd()

for i in range(1,5):  
    abc.left(35)
    abc.forward(50)
    abc.right(35)
    abc.forward(50)
    abc.right(145)
    abc.forward(50)
    abc.right(35)
    abc.forward(50)
    abc.right(10)
abc.seth(270)
abc.forward(200)
        

window.exitonclick()

