import turtle
import random
import time

LEVEL_INCREMENT = 1
start_position = {"x": 0, "y": -300}
FINISH_Y = 250  # End
FONT_SIZE = 20  # Font size
BGCOLOR = "white"
car_speed = 1
level = 1
# set screen size
HEIGHT = 500
WIDTH = 600
just_move = True
# Set up Screen
screen = turtle.Screen()
screen.screensize(WIDTH, HEIGHT, BGCOLOR)
screen.title("Przeprowadź żółwia przez ulicę")

# draw the borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-450, -380)
border_pen.down()
border_pen.pensize(3)
for side in range(4):
    if side % 2 == 0:
        border_pen.forward(900)
    else:
        border_pen.forward(760)
    border_pen.left(90)
border_pen.hideturtle()

gracz = turtle.Turtle()
gracz.shape("turtle")
gracz.speed(0)
gracz.color("green")
gracz.penup()
gracz.setposition(start_position["x"], start_position["y"])
gracz.setheading(90)

# Set turtle on the starting point
inscription = turtle.Turtle()
inscription.speed(0)
inscription.hideturtle()
inscription.penup()
inscription.setposition(-350, 350)
inscription.write(f"Level {level}", align="right", font=("Arial", FONT_SIZE, "normal"))


# Car stuff
def make_car(x=-1000, y=-1000):
    global car_speed
    car = turtle.Turtle()
    car.hideturtle()
    car.shape("square")
    car.speed(0)
    car.color(random.choice(["blue", "red", "pink", "purple", "brown"]))
    car.penup()
    car.setheading(180)
    car.setposition(random.randint(-WIDTH // 2, WIDTH // 2), random.randint(-HEIGHT // 2, HEIGHT // 2))
    car.showturtle()
    car.speed(car_speed)
    return car


cars = []
for _ in range(40):
    cars.append(make_car())
    time.sleep(0.001)


def update_level():
    global level, just_move, car_speed
    just_move = False
    level += 1
    car_speed = level
    gracz.hideturtle()
    gracz.setposition(start_position['x'], start_position['y'])
    gracz.showturtle()
    inscription.clear()
    inscription.write(f"Level {level}", align="right", font=("Arial", FONT_SIZE, "normal"))
    just_move = True


def move_forward():
    global just_move
    x = gracz.ycor()
    x += 20
    gracz.sety(x)
    print(gracz.ycor())
    if x > 350:
        update_level()
    screen.update()


def car_move(car):
    global car_speed
    x = car.xcor()
    x -= car_speed
    if x < -350:
        car.hideturtle()
        car.speed(0)
        car.setx(300)
        car.speed(car_speed)
        car.showturtle()
    else:
        car.setx(x)
    screen.update()


turtle.listen()

if just_move:
    turtle.onkey(move_forward, "Up")
while True:
    for car in cars:
        car_move(car)
