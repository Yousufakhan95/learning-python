

#A for loop lets us loop throught differntcolection of itmes
#for ex it allowles you to loop throught letter in a string 
#for varibe in a_collection:
# so for each letter will get its own line in the terminal

for letter in "Yousuf":
  print(letter)

print(" ")

# this is going to print my frendes names on each line 
friends = ["damer", "tom", "matthew"]
for friends in friends:
  print(friends)

print(" ")

#so this is going to print every number form 0 to 10 but not 10 becuase it has a lime of 10 numbers
for index in range(10):
  print(index)

print(" ")

# this going to print from 3 to 18 not 19 so it is lways 1 less
for index in range(3, 19):
  print(index)

print(" ")

#this bascilly the same as before but this time it is with range so you can shortlist more eassly if you want to
friend = ["damer", "tom", "matthew"]
for index in range(len(friend)):
  print(friend[index])

print(" ")

#so this is going print  first ideration only on the first loop
for index in range(5):
  if index == 0:
      print("first ideration")
  else:
    print("not first")