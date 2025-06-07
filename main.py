from turtle import Turtle,Screen
"""timmy is the object which is created form Turtle class"""
timmy=Turtle()
print(timmy)

# Create turtle and screen

timmy.shape("turtle")

timmy.color("red")


def hide():
    timmy.hideturtle()

# Draw a square
def square():
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)
        hide()




def triangle():
    # Move and draw triangle roof
    timmy.penup()
    timmy.goto(0, 100)  # Go to top of square
    timmy.pendown()
    # timmy.showturtle()  # Show again for triangle drawing
    timmy.goto(50, 150)
    timmy.goto(100, 100)
    hide()



def rectangel():
    timmy.forward(150)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(150)
    timmy.left(90)
    timmy.forward(50)
    hide()




user = True
while user :
    choose = input("which shape you want to draw\n").lower()
    if choose == "square" :
        square()
    elif choose=="triangle":
        triangle()
    elif choose=="rectangle":
        rectangel()
    else:
        print("please check the shape")
        user=False

#Create turtle screen
myscreen = Screen()
print("Canvas height:", myscreen.canvheight)
myscreen.exitonclick()

