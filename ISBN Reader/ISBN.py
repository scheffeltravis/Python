#  File: ISBN.py

#  Description: This program checks, given multiple lines of file input, whether
#  they are valid/invalid ISBN numbers

#  Student Name: Travis Scheffel

#  Student UT EID: TWS 529

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 2/3/2015

#  Date Last Modified: 2/4/2015

#Function checks whether the 10-digit ISBN number is valid
def validate(file_1, file_2):
  for line in file_1:

    # Strips the new line character and hyphens.
    num = line.rstrip().replace('-', "")

    isbn = []
    sum_1 = 0
    sum_2 = 0

    for i in range(0, len(num)):
      digit = num[i : i + 1]

      # Computes the sums and appends the values to the isbn digit list.
      if (digit.isdigit()):
        isbn.append(int(digit))
        sum_1 += int(digit)
      elif (digit == 'X' or digit == 'x'):
        isbn.append(10)
        sum_1 += 10

      sum_2 += sum_1

    # Checks if the length is still 10 digits.
    if (len(isbn) == 10):

      # Checks if isbn has an X or the number 10.
      if (10 in isbn):
        try:
          index = isbn.index(10)
        except ValueError:
          index = -1

        # Checks if that X is in the last index.
        if (index == 9):
          if (sum_2 % 11 == 0):
            file_2.write("{0:<17}".format(line.rstrip()) + "Valid\n")
          else:
            file_2.write("{0:<17}".format(line.rstrip()) + "Invalid\n")
        else:
          file_2.write("{0:<17}".format(line.rstrip()) + "Invalid\n")
      else:
        if (sum_2 % 11 == 0):
            file_2.write("{0:<17}".format(line.rstrip()) + "Valid\n")
        else:
            file_2.write("{0:<17}".format(line.rstrip()) + "Invalid\n")
    else:
      file_2.write("{0:<17}".format(line.rstrip()) + "Invalid\n")

def main():
  infile = open("isbn.txt", 'r')
  outfile = open("isbnOut.txt", 'w')
  
  validate(infile, outfile)

  print ("Output has been written to isbnOut.txt")

  infile.close()
  outfile.close()

main()
