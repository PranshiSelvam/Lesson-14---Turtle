import turtle 
turtle.Screen().bgcolor("purple")
tu = turtle.Turtle()

size = 0
while True:
    for i in range(4): 
        tu.forward(size+1)
        tu.left(90)
        size=size-5
    size=size+1

turtle.done()