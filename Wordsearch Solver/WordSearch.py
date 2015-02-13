
def find(puzzle, clues, length, outfile):
  # Make a list of tuples containing each letter and its row and column.
  letters = [(letter, divmod(index, length))
             for  index, letter in enumerate (puzzle)]

  # Reorder the list to represent each reading direction, and add
  # them all to a dictionary.
  lines = {}
  offsets = {'down' : 0, 'left down' : -1, 'right down' : 1}
  for direction, offset in offsets.items():
    lines[direction] = []

    for i in range(length + 1):
      for j in range(i, len(letters), length + offset):
          lines[direction].append(letters[j])

      lines[direction].append('\n')
    
  lines['left']  = letters
  lines['right'] = [i for i in reversed(letters)]
  lines['up'] = [i for i in reversed(lines['down'])]
  lines['left up'] = [i for i in reversed(lines['right down'])]
  lines['right up'] = [i for i in reversed(lines['left down'])]

  # Make strings from the letters, find the words in them and retrieve
  # their original locations.
  for direction, tup in lines.items():
    string = ''.join([i[0] for i in tup])
    for word in clues:
      if word in string:
        location = tup[string.index(word)][1]
        found = "{0:<20}".format(word) + " Row: " + "{0:<4}".format(location[0] + 1) + " Column: " + "{0:<4}".format(location[1] + 1) + " Direction: " + str(direction)
        outfile.write(found + '\n')


# Main function reads the input and defines the dimensions, clues, and puzzle;
# it then gives confirmation of output and closes the files.
def main():
  infile = open("hidden.txt", 'r')
  outfile = open("found.txt", 'w')

  lines = infile.readlines()
  dim = lines[0].rstrip()
  row = int(dim[0 : dim.index(' ')])
  col = int(dim[dim.index(' ') + 1 : len(dim)])
  words = int(lines[row + 3].rstrip())

  clues = []
  puzzle = ""
  for i in range(2, row + 2):
    puzzle += lines[i]

  for i in range(row + 4, (row + 4) + words):
    clues.append(lines[i].rstrip())
  
  puzzle = puzzle.replace(' ','')            
  length = puzzle.index('\n') + 1

  find(puzzle, clues, length, outfile)

  print ("Solutions have been written to output.txt")

  infile.close()
  outfile.close()

main()
