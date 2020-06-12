

# you whould want to store this command in a varible so it is stored

friend_or_peer = open("test_for_reading_files.py", "r")# you r means read
# insted you can also put in a which means append to that file but you cant remove 
# and you can also put r+ this can add and substractt thinges for the file
# you will also need to close a file when you open it

# this is going to output a boolean value if yes then = true
print(friend_or_peer.readable())

# this is going to print every thing in the file
print(friend_or_peer.read())

print(" ")

# this is going to print the first line in that file
print(friend_or_peer.readlines())
# if you keep going like this it is going to print then next line over so this is going print the second line
print(friend_or_peer.readlines())

#this is going to print the line that is in the square brakets
print(friend_or_peer.readlines()[1])

for friend in test_for_reading_file.readlines():
    print(friend)

# this is the close function varible.close()
friend_or_peer.close()