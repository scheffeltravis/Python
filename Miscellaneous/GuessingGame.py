import math

# Function simply introduces the guessing game.
def introduction():
  print ("Guessing Game")
  print ("\nThink of a number between 1 and 100 inclusive."
         + "\nAnd I will guess what it is in 7 tries or less.\n")

# Conducts binary search in range and accounts for user error.
def binarySearch(lo, hi, mid, count):
  offset = 0

  for count in range(1, 8):
    print ("\nGuess ", count, ":  The number you thought was ", mid)
    offset = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))

    # Binary search algorithm.
    if (offset == 0):
      print ("\nThank you for playing the Guessing Game!")
      break
    elif (offset == 1):
      hi = mid
      mid = (mid + lo) // 2
    elif (offset == -1):
      lo = mid
      mid = (mid + hi) // 2
    count += 1

  if (count > 7):
    print ("\nEither you guessed a number out of range or you had an incorrect entry.")
    
def main():
  introduction()

  lo = 1
  hi = 100
  mid = 50
  count = 1

  # Asks the user whether they are ready to play.
  answer = ""
  while (True):
    answer = input("Are you ready? (y/n): ")
    if (answer.lower() == 'n'):
      print ("Bye!")
      break
    elif (answer.lower() == 'y'):
      binarySearch(lo, hi, mid, count)
      break

main()
