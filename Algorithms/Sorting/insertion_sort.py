"""
    insertion_sort.py

    Uses insertion of elements in to the list to sort the list.

    Time Complexity: O(n**2)

    Space Complexity: O(n) total

    Stable
"""

def sort (seq):
  for i in range(1, len(seq)):
    item = seq[i]

    while (i > 0) and (seq[i - 1] > item):
      seq[i] = seq[i - 1]
      i = i - 1

    seq[i] = item

  return seq
