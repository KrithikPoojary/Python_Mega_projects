MAX_LINES = 3

print("*****Welcome to Slot machine!!!*****")

def deposit():
    while True:
        amount = input("Enter your deposit: $")   #blud we can do directly but if the value is not int then it gives error (in int(input))
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater then 0!")
        else:
            print("Amount should be entered as numbers")
    return amount

deposit()

def get_number_of_lines():
    while True:
            lines = input(f"Enter the number of line to bet on 1 - {MAX_LINES}:  ")
            if lines.isdigit():
                lines= int(amount)
                if amount > 0:
                    break
                else:
                    print("Amount should be greater then 0!")
            else:
                print("Amount should be entered as numbers")
        # return amount
