

input_for_thing = int(input("please enter a number between 1 and 12: "))
# this is a dictonary you need the equal sing and brakets
# in here you can plot a value and the meaning of it after thr colen witha space 
# the callsing can also be a string in quotes and the meaning can also be a number the number don't need quotes
month_conversions = {
  1: "Janunary",
  2: "Febuarary",
  3: "March",
  4: "April",
  5: "May",
  6: "June",
  7: "July",
  8: "August",
  9: "September",
  10: "October",
  11: "November",
  12: "December",
}

def hello():
  if input_for_thing <= int(12):
    # to aessec the dictonary you can put the name of it then .get(in here you put in the call sine)
    # there is anothere way you can put the name of the dictonary[then in square brakets put in the call sing]
    print(month_conversions.get(input_for_thing))
  else:
    print("invalid input")

hello()