#  File: CreditCard.py

#  Description: Verifies whether or not the given input is a valid credit card number or not.

#  Student Name: Travis Scheffel

#  Student UT EID: TWS 529

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 1/23/2015

#  Date Last Modified: 1/23/2015

# This function checks if a credit card number is valid
def is_valid (cc_num):
  count = 0
  total = 0

  while (cc_num != 0):
    digit = cc_num % 10
    cc_num //= 10
    count += 1
				
    if (count % 2 == 0):
      digit *= 2					

      if (digit > 9):
        digit = (digit % 10) + 1

      total += digit

    else:
      total += digit

  return (count == 15 or count == 16 and total % 10 == 0)

# This function returns the type of credit card
def cc_type (cc_num):
  num = str(cc_num)

  if (num[:4] == '6011' or num[:3] == '644' or num[:2] == '65'):
    return ("Discover")
  elif (num[:2] == '50' or num[:2] == '51' or num[:2] == '52' or
        num[:2] == '53' or num[:2] == '54' or num[:2] == '55'):
    return ("MasterCard")
  elif (num[:2] == '34' or num[:2] == '37'):
    return ("American Express")
  elif (num[:1] == '4'):
    return ("Visa")
  else:
    return ("")

def main():

  # This method asks the user to enter a 16-digit number.
  cardNumber = int(input("Enter 15 or 16-digit credit card number: "))

  count = 0

  while (cardNumber != 0):
    cardNumber //= 10
    count += 1

  if (count == 15 or count == 16):
    if (is_valid (cardNumber)):
      print ("\nValid", cc_type (cardNumber), "credit card number")
    else:
      print ("\nInvalid credit card number")
  else:
    print ("\nNot a 15 or 16-digit number")
    return
  
main()

