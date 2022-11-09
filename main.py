from art import logo
from replit import clear
# Calculator

# Add
def add(num1, num2):
  return num1 + num2

# Subtract
def subtract(num1, num2):
  return num1 - num2

# Multiply
def multiply(num1, num2):
  return num1 * num2

# Divide
def divide(num1, num2):
  return num1 / num2

# Operations
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calculate():
  print(logo)
  continue_calculation = True
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  while continue_calculation:  
    operations_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")
  
    user_answer = input(f"Type 'y' to continue calculating with {answer}, or type 'new' to start a new calculation, or type 'n' to exit program.:  ")  
    if(user_answer == 'y'):
      num1 = answer
    elif (user_answer == 'new'):
      continue_calculation = False
      clear()
      calculate()
    else:
      return print("Program ending...")
    
calculate()
