import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copy per column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # without replacement within a column
            column.append(value)
        columns.append(column)
    return columns

def deposit():
    while True:
        amount_str = input("What would you like to deposit? $")
        try:
            amount = int(amount_str)
            if amount > 0:
                return amount
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Enter numeric values only.")

def get_number_of_lines():
    while True:
        s = input(f"How many lines would you like to bet on (1–{MAX_LINES})? ")
        try:
            number_of_lines = int(s)
            if 1 <= number_of_lines <= MAX_LINES:
                return number_of_lines
            else:
                print(f"You can only enter 1 to {MAX_LINES}.")
        except ValueError:
            print("Enter numeric values only.")

def get_bet():
    while True:
        s = input(f"What would you like to bet per line? (${MIN_BET}–${MAX_BET}): $")
        try:
            bet = int(s)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        except ValueError:
            print("Enter numeric values only.")

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            end_char = " | " if i != len(columns) - 1 else "\n"
            print(column[row], end=end_char)

def spin(balance):
    number_of_lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * number_of_lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {number_of_lines} lines. Total bet: ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbols)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, number_of_lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    if winning_lines:
        print("Winning lines:", *winning_lines)
    else:
        print("No winning lines this spin.")

    return winnings - total_bet  # net change

def main():
    balance = deposit()
    while True:
        print(f"\nCurrent balance: ${balance}")
        answer = input("Press Enter to spin or 'q' to quit: ").strip().lower()
        if answer == "q":
            break
        balance += spin(balance)
        if balance <= 0:
            print("You're out of balance. Game over.")
            break
    print(f"\nYou left with ${balance}.")

if __name__ == "__main__":
    main()
