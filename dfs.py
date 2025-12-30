tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

# Recursive DFS function
def dfs_recursive(tree, node, visited=None):
  if visited == None:
    visited = set()
  visited.add(node)
  print(node)
  for child in tree[node]:
    if child not in visited:
      dfs_recursive(tree, child)

dfs_recursive(tree, 'A')