# Create a bank for the Vigenere cipher.
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def vigenere_encode (strng, passwd):
  encoded = ""
  code = []

  for i in range(len(strng)):
    j = i % len(passwd)

    code.append(passwd[j : j + 1])
  
    if (strng[i : i + 1].isalpha()):    
      shift = ord(code[i]) - ord('a')
      alpha_shift = alpha[shift : ] + alpha[ : shift]
    
      index = ord(strng[i : i + 1]) - ord('a')
      encoded = encoded + alpha_shift[index]
    else:
      code.insert(i, ' ')
      encoded = encoded + strng[i : i + 1]

  print ("\nEncoded Text: " + encoded)

def vigenere_decode (strng, passwd):
  decoded = ""
  code = []

  for i in range(len(strng)):
    j = i % len(passwd)

    code.append(passwd[j : j + 1])
  
    if (strng[i : i + 1].isalpha()):    
      shift = ord(code[i]) - ord('a')
      alpha_shift = alpha[shift : ] + alpha[ : shift]
    
      index = alpha_shift.index(strng[i : i + 1])
      decoded = decoded + alpha[index]
    else:
      code.insert(i, ' ')
      decoded = decoded + strng[i : i + 1]

  print ("\nDecoded Text: " + decoded)

def main():
  message = input ("What message do you have? ")
  line = message.strip().lower()

  key = input("What is the cipher key? ")

  while (True):
    choice = input ("\nWould you like to encode or decode the message? (e/d): ")
    if (choice.lower() == 'e'):
      vigenere_encode (line, key)
      break
    elif (choice.lower() == 'd'):
      vigenere_decode (line, key)
      break

main()
