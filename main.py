import turtle
import random
import time

LEVEL_INCREMENT = 1
START_Y = -250  # Start
FINISH_Y = 250  # End
FONT_SIZE = 20  # Font size
BGCOLOR = "white"
speed = 1

# set screen size
HEIGHT = 500
WIDTH = 600



# Set up Screen
screen = turtle.Screen()
screen.screensize(WIDTH, HEIGHT, BGCOLOR)
screen.title("Przeprowadź żółwia przez ulicę")

# draw the borders
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-450, -380)
mypen.down()
mypen.pensize(3)
for side in range(4):
    if side % 2 == 0:
        mypen.forward(900)
    else:
        mypen.forward(760)
    mypen.left(90)

gracz = turtle.Turtle()
gracz.shape("turtle")
gracz.color("green")
gracz.penup()
gracz.right(-90)
gracz.goto(0, START_Y)

# Set turtle on the starting point
napis = turtle.Turtle()
napis.hideturtle()
napis.penup()
napis.goto(-250, HEIGHT / 2 - FONT_SIZE - 5)
napis.write("Level 1", align="right", font=("Arial", FONT_SIZE, "normal"))

# Car stuff
car = turtle.Turtle()
car.shape("square")
car.color(random.choice(["blue", "red", "yellow", "pink", "purple", "brown"]))
car.penup()
car.setheading(180)
car.goto(random.randint(-WIDTH // 2, WIDTH // 2), random.randint(-HEIGHT // 2, HEIGHT // 2))
turtle.listen()


# Functions to controll our turtle
def move_left():
    gracz.left(10)


def move_forward():
    global speed
    speed += 1


def move_backward():
    global speed
    speed -= 1


def move_right():
    gracz.right(10)


# methods to async control our turtle/ binding
turtle.onkey(move_left, "Left")
turtle.onkey(move_forward, "Up")
turtle.onkey(move_backward, "Down")
turtle.onkey(move_right, "Right")

# while loop for movement and changes
while True:
    gracz.forward(speed)

    if gracz.xcor() < -450 or gracz.xcor() > 450:
        gracz.right(90)
    if gracz.ycor() < -380 or gracz.ycor() > 380:
        gracz.right(90)