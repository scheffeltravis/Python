def flip(x):
  num = list("{0:032b}".format(x))
  l = []

  for i in range(len(num)):
    if num[i] == "0":
      l.append(1)
    else:
      l.append(0)

  bit_flipped = int(''.join(str(e) for e in l), 2)

  return bit_flipped
