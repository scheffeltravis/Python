"""
    bubble_sort.py

    A naive sorting algorithm that compares and swaps adjacent elements

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable
"""

def sort (seq):
  for i in range(len(seq)):
    for j in range(1, len(seq)):
      if seq[j] < seq[j - 1]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]

  return seq
