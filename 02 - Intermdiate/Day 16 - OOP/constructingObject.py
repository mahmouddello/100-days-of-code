import turtle
timmy = turtle.Turtle()  # Object from Turtle class
myScreen = turtle.Screen()  # New object from the Screen class
########################
# Object Attributes:

print(myScreen.canvheight)
# Printing the height of the canvas (window pop up when we run code), canvheight is an attribute of myScreen object


########################
# Object methods:
timmy.shape('turtle')  # Changing the shape of the object on the screen
timmy.color('green')  # Changing the color of the shape
timmy.forward(100)  # Move the turtle forward by the specified distance.
myScreen.exitonclick()
# This method will close the screen when it detects a click, we can see a dot on screen it's our (timmy) object.
########################
