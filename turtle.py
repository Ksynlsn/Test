import turtle
wn = turtle.Screen()

def createTurtle(name, color):
    name = turtle.Turtle()
    name.color(color)
    return name
    
def drawPolygon(numSides, sideLength):
    name = input("Name your turtle")
    color = input("Choose a color")
    newTurtle = createTurtle(name, color)
    newTurtle.write(f'Hi, my name is {name}')
    newTurtle.penup()
    newTurtle.right(90)
    newTurtle.forward(50)
    newTurtle.pendown()
    for i in range(numSides):
        newTurtle.forward(sideLength)
        newTurtle.right(360/numSides)
        
        
drawPolygon(4, 20)