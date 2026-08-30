print("*****Welcome to Slot machine!!!*****")

def deposit():
    while True:
        amount = int(input("Enter your deposit: $"))
        if amount > 0:
            break
        