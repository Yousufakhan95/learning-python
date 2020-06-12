
print(" ")
print("Welcome to this addition calulator!")
print(" ")

#these are going to store values of the two numbers
num1 = input("enter a number: ")
num2 = input("enter another number: ")

# this is the math part
#you need float or else it is going to convert it in to a string
# you can also use int but that is only for whole numbers
# float can take decibels
result = float(num1) + float(num2)

#this is going to print the final result
print(result)