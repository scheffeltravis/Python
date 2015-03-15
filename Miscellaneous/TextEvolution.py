import string
import random
import time

# Create a cache of all character choices in string format.
characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

target = input("Enter your target text: ")
attempt = ''.join(random.choice(characters) for i in range(len(target)))
new_attempt = ''

completed = False

generation = 0

# This simply runs through each character and replaces it randomly until
# the correct one is found.
while (completed == False):
  print(attempt)
  new_attempt = ''
  completed = True

  for i in range(len(target)):
    if (attempt[i] != target[i]):
      completed = False
      new_attempt += random.choice(characters)
    else:
      new_attempt += target[i]

  generation += 1
  attempt = new_attempt

  # This simply adjusts the time in between each loop for visibility.
  time.sleep(.1)

print("Target matched! That took " + str(generation) + " generation(s)")
