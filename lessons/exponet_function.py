
# this going to print 8 because 2 to the power 3 is 8
# the dual mutiplytion sing is one of the exponet function
print(2**3)

print(" ")

#pow means power number
#index is the thing in the brakets is it so it is going in that order
# so it is going to run the base number throught it slef the same number of time as the pow num
# so if it is 2 to the power of 3 it is going to times 2 by it slef 3 times
def rasie_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result
# the 3 , 4 is the index
print(rasie_to_power(3, 4))