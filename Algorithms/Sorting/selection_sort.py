"""
    selection_sort.py

    Uses in-place comparision to sort the list

    Time Complexity:  O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable
"""

def sort(seq):
  for i in range(0, len(seq)):
    iMin = i

    for j in range(i + 1, len(seq)):
      if seq[j] < seq[iMin]:
        iMin = j
      if i != iMin:
        seq[i], seq[iMin] = seq[iMin], seq[i]

  return seq
