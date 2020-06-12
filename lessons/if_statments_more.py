

#
def max_num(num1, num2, num3):
   # >= is means greater than or equal to and these to compare
   # if this is right this means num1 is the greates number
   # you can also do compare stringes
   if num1 >= num2 and num1 >= num3:
      return num1
   elif num2 >= num1 and num2 >=num3:
      return num2
   else:
      return num3

# this is going in order of num1 and etc and plot them in
print(max_num(3, 8, 2))
print("is there greatest number")

# == this means equal to
# != this means not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to