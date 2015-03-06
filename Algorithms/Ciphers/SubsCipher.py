# Create a bank for the substitution cipher.
cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v','t',
            'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']

def substitution_encode (strng):
  encoded = ""

  for i in range(len(strng)):
    if (strng[i : i + 1].isalpha()):
      index = ord(strng[i : i + 1]) - ord('a')
      encoded = encoded + cipher[index]
    else:
      encoded = encoded + strng[i : i + 1]

  print ("\nEncoded Text: " + encoded)

def substitution_decode (strng):
  decoded = ""

  for i in range(len(strng)):
    if (strng[i : i + 1].isalpha()):
      index = cipher.index(strng[i : i + 1]) + ord('a')
      decoded = decoded + chr(index)
    else:
      decoded = decoded + strng[i : i + 1]

  print ("\nDecoded Plain Text: " + decoded)

def main():
  message = input ("What message do you have? ")
  line = message.strip().lower()

  while (True):
    choice = input ("\nWould you like to encode or decode the message? (e/d): ")
    if (choice.lower() == 'e'):
      substitution_encode (line)
      break
    elif (choice.lower() == 'd'):
      substitution_decode (line)
      break

main()
