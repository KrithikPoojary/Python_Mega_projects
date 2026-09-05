import turtle
import time
import random
WIDTH , HEIGHT = 500 , 500
COLORS  = ['yellow' , 'cyan' , 'pink' , 'brown' , 'black' , 'red' , 'blue' , 'green' , 'purple' , 'orange']
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

# race = turtle.Turtle()
# race.penup()  #NOt give us line 
# race.speed(1)
# race.shape('turtle')
# race.color("pink")
# race.forward(100)
# race.pendown()   #Give the line
# race.left(90)
# race.forward(100)
# race.right(90)
# race.backward(100)
# # time.sleep(3)

random.shuffle(COLORS)
colors = COLORS[:racer]    #We are slicing the COLOUR variables up to user input.
print(colors)