data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]
def print_transactions(transactions):
  for transaction in transactions:
    amount = transaction[0]
    statement = transaction[1]
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(f"Total deposited: {total_deposited}")
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawals = sum(withdrawals)
  print(f"Total withdrawals: {total_withdrawals}")
  balance = round(total_deposited + total_withdrawals, 2)
  print(f"Balance: {balance}")
  print()

def analyze_transactions(transactions):
  amounts = [transaction[0] for transaction in transactions]
  amounts.sort()
  largest_withdrawal = amounts[0]
  largest_deposit = amounts[-1]
  print(f"Largest withdrawal: {largest_withdrawal}")
  print(f"Largest deposit: {largest_deposit}")
  deposits = [amount for amount in amounts if amount >= 0]
  total_deposits = sum(deposits)
  if len(deposits) > 0:
    average_deposits = round(total_deposits/(len(deposits)),2)
  else:
    average_deposits = 0
  print(f"Average deposits = {average_deposits}")
  withdrawals = [amount for amount in amounts if amount < 0]
  total_withdrawals = sum(withdrawals)
  if len(withdrawals) > 0:
    average_withdrawals = round(total_withdrawals/(len(withdrawals)), 2)
  else:
    average_withdrawals = 0
  print(f"Average withdrawals: {average_withdrawals}")
  print()

while True:
  print("Select option(print, analyze or stop):")
  choice = input()
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    break
  else:
    print("Invalid choice")