from math import sqrt

# This function checks if a given number is prime.
def is_prime (n):
  limit = int(sqrt(n) + 1)
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div = div + 1
  return True

# This function computes the different pairs of primes which make up a number.
def pairs (lower, upper):
  pair = ""
  count = 0
  maximum = 0

  # Computes the first prime in a number and prints out the pair with its difference.
  for i in range(lower, upper + 1, 2):

    # Accounts for commutativity and the number one not being prime.
    for j in range(2, (i // 2) + 1):
      if (is_prime (j) and is_prime (i - j) and (i - j != 1)):
        pair += " = " + str(j) + " + " + str(i - j)
        count += 1

      # This simply counts the maxmimum number of pairs of primes for a single number.
      if (count > maximum):
        maximum = count
      
    print (str(i) + pair)
    pair = ""
    count = 0

  print ("\nThe maximum number of pairs is", maximum)

def main():

  # Accounts for user error when entering a useful range.
  while True:
    lower = int(input("Enter lower limit: "))
    upper = int(input("Enter upper limit: "))
    print ("")

    if (lower >= 4) and (lower % 2 == 0) and (lower <= upper) and (upper % 2 == 0):
      break

  pairs (lower, upper)

main()
