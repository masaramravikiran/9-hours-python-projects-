import random

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

symbol_value = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 2
}

def check_winnings(columns, lines,bet ,values):
  winnings = 0
  winning_lines = []

  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol:
        break
      else:
        winnings += values[symbol] *bet
        winning_lines.append(line + 1)
  return winnings,winning_lines


def get_slot_machine_spin(rows,clos,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
          all_symbols.append(symbol)
    
    columns = [] 
    for col in range(col):
      columns = []
      current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(all_symbols)
      current_symbols.remove(value)
      columns.append(value)
      
    columns.append(columns)
    
    return columns
  
def print_slot_machine(columns):
  for row in range(len(columns[0])):
      for i, column in enumerate(columns):
        if i != len(columns) -1:
          print(column[row], end= "|")
        else:
            print(column[row], end="")
            
      print()
def deposit():
    while True:
      amount = input("What would you like to deposit? $")
      if amount.isdigit():
        amount = int(amount)
        if amount > 0:
          break
        else:
          print("amount must be greater than 0.")
      else:
        print("Invalid input. Please enter a number.")
    return amount
  
def get_number_of_lines():
  while True:
      lines = input(("Enter the number of lines to bet on (1-")+ str(MAX_LINES) + ")? ")
      if lines.isdigit():
        lines = int(lines)
        if 1 <= lines <= MAX_LINES:
          break
        else:
          print("Enter a valid number of lines.")
      else:
        print("Invalid input. Please enter a number.")
  return lines

def get_bet():
  while True:
      amount = input("What would you like to bet on each line? $")
      if amount.isdigit():
        amount = int(amount)
        if MIN_BET <= amount <= MAX_BET:
          break
        else:
          print("amount must be between ${MIN_BET} - ${MAX_BET} .")
      else:
        print("Invalid input. Please enter a number.")
  return amount
  
def spin():
  balance = deposit()
  lines = get_number_of_lines()
  while True:
      bet = get_bet()
      total_bet = bet * lines
      if total_bet > balance:
        print("You do not have enough to bet that amount, your current balance is : ${balance}")
      else:
          break
  print(f"YOu are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")
    
  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings,winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"you won ${winnings}.")
  print(f"You won on", *winning_lines)
  return winning_lines - total_bet

def main():
    balance = deposit()
    while True:
      print(f"Your current balance is: ${balance}")
      answer = input("press enter to spin (q to quit).")
      if spin == "q":
        break
      balance += spin()
      
      print("YOU left with ${balance}")
main()
