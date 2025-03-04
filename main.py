import random
from traceback import print_tb

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows,cols,symbols):
    #print(rows, cols,symbols)
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            #print(all_symbols)

    columns= []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            #print(column)

        columns.append(column)
        #print ("columns", columns)
    return columns

def print_slot_machine(columns):
    print(columns[0])
    for row in range(len(columns[0])):
            for i,column in enumerate (columns):
                if i != len(columns)-1:
                    print(column[row], " | ")
                else:
                    print(column[row])


def deposit():
    while True:
        amount = input("How much would you like to deposit? £ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. ")
        else:
            print("Please enter a number: ")

    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on (1-" + str (MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines. ")
        else:
            print("Please enter a number: ")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? £ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:

                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}. ")
        else:
            print("Please enter a number: ")

    return amount






def main():
    balance = deposit()

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet *lines
        if total_bet > balance:
            print(f"You do not have enough money to bet tha amount,your current balance is £{balance} ")
        else:
            break
    print(f"You are betting £{bet} on {lines} lines. Total bet is  equal to : £{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    #print(slots)
    print_slot_machine(slots)





main()


