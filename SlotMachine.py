def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

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

if __name__ == '__main__':
    main()