from collections import deque

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

def bfs(tree, node):
  visited = set()
  queue = deque([node])  # Initialize the queue with the starting node

  while queue:  # While there are still nodes to process
    node = queue.popleft()  # Dequeue a node from the front of the queue

    if node not in visited:  # Check if the node has been visited
      visited.add(node)  # Mark the node as visited
      print(node)  # Output the visited node

      # Enqueue all unvisited children of the current node
      for child in tree[node]:
        if child not in visited:
          queue.append(child)  # Add unvisited children to the queue

bfs(tree, 'A')