MAX_LINES = 3
MAX_BET = 100        #Here capitals are constants...
MIN_BET = 30

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


def get_number_of_lines():
    while True:
            lines = input(f"Enter the number of lines to bet on 1 - {MAX_LINES}:  ")
            if lines.isdigit():
                lines= int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter the valid number.")
            else:
                print("lines should be entered as numbers")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter the Amount of bet ({MIN_BET}$-{MAX_BET}$) on each line:  ")
        if bet.isdigit():
            bet= int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter the bet Amount between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Bet should be entered as numbers")
    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    Total_bet = bet*lines
    print(f"You are betting ${bet} on {lines} lines and Your total bet amount is {Total_bet}$")
    print(balance , lines,bet)

main()