

#
print(" ")
print("Welcome to this translator")
print("this transltor will translate from english to my plop language")
def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.lower() in "aeiou":
      if letter.isupper():
        translation = translation + "W"
      else:
        translation = translation + "w"
    else:
      translation = translation + letter
  return translation

print(translate(input("enter a phrase: ")))
print("this is your phrase in the plop language")