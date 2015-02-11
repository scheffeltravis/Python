def flipping_bits(x):
  num = list("{0:032b}".format(x))
            
  l = [1 if num[i] == "0" else 0 for i in range(len(num))]
  bit_flipped = int(''.join(str(e) for e in l), 2)

  print("\nThe flipped bit number is", bit_flipped)

def main():
  given = int(input("Enter a number: "))
  
  flipping_bits(given)

main()
