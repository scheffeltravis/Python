"""
    heap_sort.py

    Uses the max heap data structure implemented in a list.

    Time Complexity: O(n * log n)

    Space Complexity: O(1) Auxiliary

    Unstable
"""

def max_heapify (seq, i, n):
  left = 2 * i + 1
  right = 2 * i + 2

  if left <= n and seq[left] > seq[i]:
    largest = left
  else:
    largest = i

  if right <= n and seq[right] > seq[largest]:
    largest = right

  if largest != i:
    seq[i], seq[largest] = seq[largest], seq[i]
    max_heapify (seq, largest, n)

def build_heap (seq):
  n = len(seq) - 1

  for i in range(n // 2, -1, -1):
    max_heapify (seq, i, n)

def sort (seq):
  build_heap (seq)
  heap_size = len(seq) - 1

  for i in range(heap_size, 0, -1):
    seq[0], seq[i] = seq[i], seq[0]
    heap_size = heap_size - 1

    max_heapify (seq, 0, heap_size)

  return seq
