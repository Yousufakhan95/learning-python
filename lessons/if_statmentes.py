
# if the is false it wont print any thing
is_male = True
is_tall = False

# you have to have that colen
# is_male is true that is why it is print it 
#this is going to actavate onlt if one or both of the varibels are true
#you chould put a or that means only one of thee values has to be true
if is_male and is_tall:
  # you have to have that indationg
  print("you are a male and tall")
  # if is like a in between a else andd a if
  # you have to put brakets after the and notd 
elif is_male and not(is_tall):
  print("your a male and not tall")
elif is_tall and not(is_male):
  print("you are tall but not male")
  # this works if the if statment is false so it is s back up
else:
  print("you are not a male and not tall")