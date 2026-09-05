import turtle
import time

WIDTH , HEIGHT = 500 , 500

def user_ask():

    while True:

        user = input('Enter the Number of turtle you want to race (2-10): ')
        if user.isdigit():
            user = int(user)

        else:
            print('Enter the Numbers only!')
            continue
        if 2<= user <= 10:
            return user
        else:
            print("Please enter the number with in the range: ")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle_Race")

racer = user_ask()
init_turtle()

race = turtle.Turtle()
race.speed(1)
race.forward(100)
race.left(90)
race.forward(100)
race.right(90)
race.backward(100)
# time.sleep(3)

