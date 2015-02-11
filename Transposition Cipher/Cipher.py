#  File: Cipher.py

#  Description: This program takes in file input, transposes the letters into a
#  different sequence, and outputs the ecrypted/decrypted message.

#  Student Name: Travis Scheffel

#  Student UT EID: TWS 529

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 2/2/2015

#  Date Last Modified: 2/3/2015

# Function which encrypts input from one file, and outputs it to another.
def encrypt(file_1, file_2):
  for line in file_1:
    line = line.rstrip()
    even = ""
    odd = ""

    for i in range(0, len(line)):      
      if (i % 2 != 0):
        odd += line[i : i + 1]
      else:
        even += line[i : i + 1]
      i +=1

    file_2.write(odd + even + "\n")

  print ("\nEncrypted message written to output.txt")

#Function which dencrypts input from one file, and outputs it to another.
def decrypt(file_1, file_2):
  for line in file_1:
    line = line.rstrip()
    decrypted = ""
    odd = ""
    even = ""

    for i in range(0, len(line)):
      odd = line[0 : len(line) // 2]
      even = line[len(line) // 2 : len(line)]
      n = (i // 2)

      if (i % 2 == 0):
        decrypted += even[n : n + 1]
      else:
        decrypted += odd[n : n + 1]

    file_2.write(decrypted + "\n")

  print ("\nDecrypted message written to output.txt")

# User decides whether the information should be enrypted or decrypted.
def main():
  action = input("Do you want to encrypt or decrypt? (E / D): ")

  infile = open("input.txt", 'r')
  outfile = open("output.txt", 'w')

  if (action == 'E' or action == 'e'):
    encrypt(infile, outfile)
  elif (action == 'D' or action == 'd'):
    decrypt(infile, outfile)
  else:
    print ("\nWrong input. Bye.")

  infile.close()
  outfile.close()

main()
