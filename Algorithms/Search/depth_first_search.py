"""
    depth_first_search.py

    Starts at a selected node (root) and explores the branch
    as far as possible before backtracking.

    Time Complexity: O(E + V)
        E = Number of edges
        V = Number of vertices (nodes)
"""

def search (graph, start, path = []):
  if (start not in graph) or (graph[start] == None) or (graph[start] == []):
    return None

  path = path + [start]

  for edge in graph[start]:
    if (edge not in path):
      path = search (graph, edge, path)

  return path
