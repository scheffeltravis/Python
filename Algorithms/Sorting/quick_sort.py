"""
    quick_sort.py

    Uses partitioning to recursively divide and sort the list

    Time Complexity: O(n**2)

    Space Complexity: O(n) Auxiliary

    Unstable
"""

def sort (seq):
  if len(seq) <= 1:
    return seq
  else:
    pivot = seq[0]
    left, right = [], []

    for i in seq[1:]:
      if i < pivot:
        left.append(i)
      else:
        right.append(i)

  return sort (left) + [pivot] + sort (right)
