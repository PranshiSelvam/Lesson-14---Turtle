import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
tu = turtle.Turtle()
sides = 5
angles = 360/sides
distance = 50
for i in range (sides): 
    tu.forward(distance)
    tu.right(angles)
turtle.done()




