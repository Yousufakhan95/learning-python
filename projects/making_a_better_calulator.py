# this showes that your taking in input then using if statments so you have a program

num1 = float(input("enter your first number: "))
op = input("please enter your operator: ")
num2 = float(input("enter your second number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2) 
elif op == "*":
  print(num1 * num2)
elif op == "/":
  print(num1 / num2) 
else:
  print("invalid operation")