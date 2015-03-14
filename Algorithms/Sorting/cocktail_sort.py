"""
    cocktail_sort.py

    Walk the list bidirectionally, swapping neighbors if one should come
    before/after the other.

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable
"""

def sort(seq):
  lower = -1
  upper = len(seq) - 1
  swapped = True

  while swapped:
    swapped = False
    lower += 1

    for i in range(lower, upper):
      if seq[i] > seq[i + 1]:
        seq[i], seq[i + 1] = seq[i + 1], seq[i]
        swapped = True

    if not swapped:
      break

    swapped = False
    upper -= 1

    for i in range(upper, lower, -1):
      if seq[i] < seq[i - 1]:
        seq[i], seq[i - 1] = seq[i - 1], seq[i]
        swapped = True

  return seq
