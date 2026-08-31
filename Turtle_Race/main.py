import turtle

WIDTH , HEIGHT = 500 , 500


def user_ask():

    while True:

        user = input('Enter the Number of turtle you want to race (2-10): ')
        if user.isdigit():
            user = int(user)

        