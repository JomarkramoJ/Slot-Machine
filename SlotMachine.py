import random
import time

def spin_row():
    symbols = ['🍇', '🍊', '🥝', '🔔', '💵']
    weights = [10, 10, 5, 1, 0.1] 
    return random.choices(symbols, weights=weights, k=3)

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍇':
            return bet * 2
        elif row[0] == '🍊':
            return bet * 5
        elif row[0] == '🥝':
            return bet * 7
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '💵':
            return bet * 20
    return 0

def spinning_effect():
    symbols = ['🍇', '🍊', '🥝', '🔔', '💵']
    for _ in range(4):
        row = random.choices(symbols, k=3) 
        print_row(row)
        time.sleep(0.5)

def main():

    print("******************************")
    print("   Welcome to Slot Machine")
    print("  Symbols: 🍇 🍊 🥝 🔔 💵")
    print("******************************")

    deposit = int(input("How much would you like to deposit? "))
    balance = deposit

    while balance > 0:
        print(f"Current balance: 💲{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Balance")
            continue

        if bet <= 0:
            print("Bet must be grater than 0")
            continue

        balance -= bet

        print("Spinning...\n")
        spinning_effect()
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won💲{payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        if balance <= 0:
            print("You are now broke")
            break

        play_again = input(f"You have💲{balance} Do you want to play again? (Y/N): ").upper()

        if play_again == 'Y':
            continue

        else:
            print("Thank you for playing!")
            break

if __name__ == '__main__':
    main()