
def main():

  # Open the given file to read input.
  infile = open ("Census_2009.txt", "r")
  pop_num = []
  count = 0

  # Runs through all lines of the given file and appends the values to a list.
  for line in infile:
    if (count == 0):
      count += 1
      continue
    else:
      count += 1
      word_list = line.strip().split()
      pop_num.append (word_list[-1])

  # Define an empty dictionary to populate.
  freq = {}

  # Populate the library with the number of values which begin a certain digit.
  for i in range(count - 1):
    pop_num[i] = int(pop_num[i]) // (10 ** (len(pop_num[i]) - 1))
    digit = pop_num[i]

    if digit in freq:
      freq[digit] = freq[digit] + 1
    else:
      freq[digit] = 1

  # Print out the digits and their frequencies in the given format.
  print ("Digit   Count     %")
  for digit in freq:
    percent = (freq[digit] / count) * 100
    
    print ("{0:<9}".format(digit) +
           "{0:<9}".format(freq[digit]) +
           "{0:.2f}".format(percent))

  # Close the input file.
  infile.close()

main()
