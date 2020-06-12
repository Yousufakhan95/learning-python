

print(" ")
print("Who ever is entering the secret word does not get to guess")

secret_word = input("Please enter a secret word: ")
type_of_word = input("Please enter a reffence of the word that you are using: ")
guess = ""
num_guess = 0
guess_lit = 3
out_of_guess = False
num_line = 0

# for ex i am using this wile loop to print a space in every line for 90 lines
while num_line != 180:
  print(" ")
  num_line += 1

print("You only have 3 trys after it is game over")
print("this is a reffence to the word that your guessing " + "'" + type_of_word + "'")

# this is a function for the number of tryes the player has had and also integrates with the next wile loop too
while guess != secret_word and not(out_of_guess):
  if num_guess < guess_lit:
    guess = input("please enter a guess: ")
    num_guess += 1
  else:
    out_of_guess = True

# this decides if you won or lost
if out_of_guess:
  print("you lost the game :(")
else:
  print("!!You Guessed The Right Word!!")
  print("!!You Won!!")