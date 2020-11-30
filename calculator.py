from replit import clear
from art import logo
print(logo)


def add(x,y):
  return x + y

def subtract(x,y):
  return x - y    

def multiply(x,y):
  return x * y

def divide(x,y):
  return x/y

def calc(a,b,operator):
  if(operator == "+"):
    result = add(a,b)
  elif(operator == "-"):
    result = subtract(a,b)
  elif(operator == "*"):
    result = multiply(a,b)
  elif(operator == "/"):
    result = divide(a,b)
  print(f"Result: {result}")  
  should_continue = input("use result in next calculation (y,n)? ")
  if(should_continue == "y"):
    operator = input("Operator? ")
    b = float(input("Second number? "))
    calc(result,b,operator)

  elif(should_continue == "n"): 
    clear() 
    return

#print(art.logo)

while True:

  a = float(input("First number? "))
  operator = input("Operator? ")
  b = float(input("Second number? "))

  result =  calc(a,b,operator)
