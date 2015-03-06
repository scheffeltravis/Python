"""
    merge_sort.py

    Uses divide and conquer to recursively divide and sort the list

    Time Complexity: O(n*log n)

    Space Complexity: O(n) Auxiliary

    Stable
"""

def merge (left, right):
  result = []
  i, j = 0, 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result += left[i:]
  result += right[j:]
  return result

def sort (seq):
  if len(seq) <= 1:
    return seq
    
  middle = len(seq) // 2
  left = sort (seq[:middle])
  right = sort (seq[middle:])

  return merge (left, right)

    
