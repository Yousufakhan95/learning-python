


#so this is kinda like a fail safe if the top code doesent work you have a back up in except
# but this can also print out what went wronge and where
try:
  value = 10/0
  number = int(input("Enter a number: "))
  print(number)
# you can have mutipel ececpt statements for one try statment
# you have to have the colen beside at the end
except ZeroDivisionError as err:
  # it shoukld be indented in the statements
  print("err")
  # this is just going to print the error because we made zerodividionerron in to err
except ValueError:
  print("invaled input")