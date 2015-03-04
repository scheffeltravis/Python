"""
    shell_sort.py

    Comparision sort that sorts far away elements first to sort the list

    Time Complexity:  O(n**2)

    Space Complexity: O(1) Auxiliary

    Unstable
"""

def sort (seq):
  splits = [x for x in range(len(seq) // 2, 0, -1)]

  for split in splits:
    for i in range(split, len(seq)):
      pivot = seq[i]
      j = i
      
      while j >= split and seq[j - split] > seq[j]:
        seq[j] = seq[j - split]
        j -= split

      seq[j] = pivot

  return seq
