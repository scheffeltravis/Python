"""
    quick_sort_in_place.py

    Uses (three way partitioning to recursively divide and sort the list

    Time Complexity: O(n**2)

    Space Complexity: O(n) Auxiliary

    Unstable
"""

from random import randrange

def partition (seq, left, right, pivot):
  value = seq[pivot]
  seq[pivot], seq[right] = seq[right], seq[pivot]
  index = left

  for i in range(left, right):
    if seq[i] < value:
      seq[i], seq[index] = seq[index], seq[i]
      index += 1

  seq[index], seq[right] = seq[right], seq[index]

  return index

def sort (seq, left, right):
  if len(seq) <= 1:
    return seq
  elif left < right:
    start = randrange(left, right)
    pivot = partition(seq, left, right, start)
    sort (seq, left, pivot - 1)
    sort (seq, pivot + 1, right)

    return seq
