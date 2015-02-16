from itertools import count
from collections import namedtuple

# Define the directional steps.
step  = namedtuple("step", ["dx", "dy"])
right = step( 1,  0)
down  = step( 0,  1)
left  = step(-1,  0)
up    = step( 0, -1)

# Use the directional steps along with an increment to assign values.
def steps_from_center():
  for n in count(start = 1):
    if n % 2:
      yield right
      for i in range(n):
        yield down
      for i in range(n):
        yield left
    else:
      yield left
      for i in range(n):
        yield up
      for i in range(n):
        yield right

# Determines the location of the number, and prints out all surrounding numbers.
def find(dim, num, spiral):
  for i in range(dim):
    for j in range(dim):
      if (spiral[i][j] == num):
        if (i != 0 and i != (dim - 1) and j != 0 and j != (dim - 1)):
          print ()
          print (spiral[i - 1][j - 1], spiral[i - 1][j], spiral[i - 1][j + 1])
          print (spiral[i][j - 1], spiral[i][j], spiral[i][j + 1])
          print (spiral[i + 1][j - 1], spiral[i + 1][j], spiral[i + 1][j + 1])
        else:
          print ("Number on outer edge!")

def main():

  # Asks the user for the dimensions and number.
  dim = int(input("What dimension matrix do you need? "))
  num = int(input("What number are you looking for? "))

  # Make sure the dimensions are the nearest odd integer.
  if (dim % 2 != 1):
    dim += 1

  # Create an empty 2D array/list to populate.
  spiral = [[0 for _ in range(dim)] for _ in range(dim)]

  # Start with the integer 1 in the center.
  x = y = dim // 2
  spiral[y][x] = 1

  # Assign all other spiral values from the center.
  for i, step in enumerate(steps_from_center(), start = 2):
    if i > (dim ** 2):
      break
    else:
      x += step.dx
      y += step.dy
      spiral[y][x] = i

  find(dim, num, spiral)
  
main()
