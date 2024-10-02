import random

def spin_row():
    symbols = ['🍇', '🍊', '🥝', '🔔', '💵']
    
    return[random.choice(symbols) for _ in range(3)]

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

def main():
    balance = 100

    print("******************************")
    print("   Welcome to Slot Machine")
    print("  Symbols: 🍇 🍊 🥝 🔔 💵")
    print("******************************")

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

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        peyout = get_payout(row, bet)

if __name__ == '__main__':
    main()