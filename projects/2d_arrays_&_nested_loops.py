

#there are lists in a list so we are creating a grid 
#so creating lists in a list python is going to think of that as a grid
#so if it think of it like a grid you can use functions like row and col
#standing for row and column
number_grid = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]

# this iassecing the grid so the first grid bracket is the x and the second is the y axies
print(number_grid[2][1])

print(" ")

#this is a nested loop so a for loop in a for loop
# so this is going to print every number in the grid in the order it is set in and each object is going to get its own line in terminal
for row in number_grid:
  for col in row:
    print(col)