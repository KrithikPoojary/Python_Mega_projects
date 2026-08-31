import turtle

WIDTH , HEIGHT = 500 , 500
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("Turtle_Race")

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

user_ask()