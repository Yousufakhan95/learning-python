# any this that is in this "" is a string
# you can also use single quotes
print("helloworld")

print(" ")

# the \n means it is a new line
print("hello\nworld")

print(" ")

# after the backslash whatever is there Python will take that literately
# so this is will print hello"world
print("hello\"world")

print(" ")

# and this will just print a backlash this can also be applied with a normal front slash
print("hello\world")

print(" ")

# over here we are just printing a varibel
hi = "helloworld"
print(hi)

print(" ")

# this will add the varibel to the string that is in the quotes
# you have to use the plus sing + to merge the strings together
world = "hello"
print(world + "world")

print(" ")

# this is bascily the same as one of the other ones that i did
# the .lower() is a "function" that makes every thing lower case
# and you dont put anything in the brackets for this use
enter = "HELLO"
print(enter.lower())

print(" ")

# this is bascily the same as the last function but it makes every thing upper case
got = "hello"
print(got.upper())

print(" ")

# this is going to return a true or false statement if the text is upper or lower
# so this is going to return false because all the letters are upper
store = "HELLO"
print(store.islower())

print(" ")

# this is going to return a true or false statement if the text is upper or lower
# so this is going to return false because all the letters are lower
app = "hello"
print(app.isupper())

print(" ")


# this is going to make it lower then check so the ans will be true
zinc = "HELLO"
print(zinc.lower().islower())

print(" ")

# this going to make the upper then check if it so the ans will be true
the = "hello"
print(the.upper().isupper())

print(" ")

# this len() function counts the number chareters in the text then prints it out
bonjour = "Helloworld"
print(len(bonjour))

print(" ")

# you can do this too for the pas function and this function counts spaces too
print(len("helloworld"))

print(" ")

# this print out a specific character in the console
# remember that python starts counting from zero
# so this will print "h"
lol = "helloworld"
print(lol[0])

print(" ")

# this function will tell us the index number for the character in in the text
yass = "helloworld"
print(yass.index("w"))

print(" ")

# this is basically the same as last time but this one tells you where that word starts
# if you put some this that in not in the text that is going to throw a error
mac = "helloworld"
print(mac.index("world"))


print(" ")

# this function replaces the part of the text that you want to replace
# .replace("the this that you want to replace", "the new thing")
micro = "helloworld"
print(micro.replace("hello", "Bye"))
