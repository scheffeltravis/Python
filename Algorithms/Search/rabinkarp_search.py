"""
    rabinkarp_search.py

    Search for a substring in a given string, by comparing hash values
    of the strings.

    Time Complexity: O(n * m)

    Space Complexity: O(n)
"""

from hashlib import md5

def search(s, sub):
  n, m = len(s), len(sub)
  hsub_digest = md5(sub).digest()
  offsets = []

  if (m > n):
    return offsets

  for i in range(n - m + 1):
    if (md5(s[i:i + m]).digest() == hsub_digest):
      if (s[i:i + m] == sub):
        offsets.append(i)

  return offsets
