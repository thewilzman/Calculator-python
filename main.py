from replit import clear
from art import logo 


# Calculator 

#add

def add(n1, n2):
  return n1 + n2

#substract

def substract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1/n2

operations = {"+": add,
              "-": substract,
              "*": multiply,
              "/": divide
             } 

def calculator():
  
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations: #prints the keys symbols of the dictionary
    print (symbol)
  
  should_continue = True #flag condition
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol] #the value of the key is the function
    answer = calculation_function(num1, num2) #passing num1 and num2 as arguments to the function
    print(f"{num1} {operation_symbol} {num2} = {answer}") #prints the result of the operation
  
    if input(f"Type'y'to continue calculating with {answer},or type 'n' to start  a new calculation \n") == "y": 
      num1 = answer
    else:
      should_continue = False #flag condition turns false
      clear()
      calculator() #recursion of the function
      
calculator() # calling the define function 


    


  
  