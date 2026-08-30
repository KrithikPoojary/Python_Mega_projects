print("*****Welcome to Slot machine!!!*****")

def deposit():
    while True:
        amount = int(input("Enter your deposit: $"))
        if amount > 0:
            break
        else:
            print("Amount should be greater then 0!")
    return amount

deposit()