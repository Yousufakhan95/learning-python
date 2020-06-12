

#
luck_numbers = [3, 50, 95, 8, 90, 33]
friends  =["thomas", "damer", "matthew", "matthew2", "no_more_friends"]

#this going to print the whole list
print(friends)

print(" ")

# this function is just going to merg the two list
#you can put qumas at the end of luck_numbers and it can add andouther list with it
friends.extend(luck_numbers)
print(friends)

hello = ["thomas", "damer", "matthew", "matthew2", "no_more_friends"]

# this function basiccly adds another word to the list it is going add it to the end
hello.append("world")
print(hello)

print(" ")

#this function is going to add the new string in to the list and where you tell it to go in the list
hello.insert(1, "jim")
print(hello)

print(" ")

#this going to remove a string from a list that you tell it to
hello.remove("jim")
print(hello)

print(" ")

apple = ["thomas", "damer", "matthew", "matthew2", "no_more_friends"]
print(apple)

# this going to clear the whole list you dont have to put any thing in the brackets
apple.clear()
print(apple)

print(" ")

say = ["thomas", "damer", "matthew", "matthew2", "no_more_friends"]

#this function is just going to "pop" out the last string in the list 
say.pop()
print(say)

print(" ")

# this going to give you the index of a value that you enterd in the brakets
# if you entered a value that is not in the list it will spit out a error
print(say.index("thomas"))

print(" ")

key = ["thomas", "damer", "matthew", "matthew2", "matthew2", "no_more_friends"]

#this function is going to count how many times is the string repating that you enterd
# so this is going to say 2 and if there is only one it is going to say 1
print(key.count("matthew2"))

print(" ")

# this going to sort the list in apbical order
#if the list only have numbers it is going to order them in assending order
key.sort()
print(key)

print(" ")

# this going to reverse the order of the list not in any order it is just going to flip it
# for number it is the same
key.reverse()
print(key)

print(" ")

# this is just going to make a copy of the list and store in a new varibel that you made
key2 = key.copy()
print(key2)

print(" ")
