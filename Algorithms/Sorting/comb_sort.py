"""
    comb_sort.py

    Improves on bubble sort by using a gap sequence to remove swapping instances.

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable
"""

def sort(seq):
  gap = len(seq)
  swap = True

  while gap > 1 or swap:
    gap = max(1, int(gap / 1.25))
    swap = False

    for i in range(len(seq) - gap):
      if seq[i] > seq[i + gap]:
        seq[i], seq[i + gap] = seq[i + gap], seq[i]
        swap = True

  return seq
