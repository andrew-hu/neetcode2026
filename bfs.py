from collections import deque

def bfs(tree, start):
  visited = set()
  queue = deque([start])  # Initialize the queue with the starting node

  while queue:  # While there are still nodes to process
    node = queue.popleft()  # Dequeue a node from the front of the queue

    if node not in visited:  # Check if the node has been visited
      visited.add(node)  # Mark the node as visited
      print(node)  # Output the visited node

      # Enqueue all unvisited neighbors (children) of the current node
      for neighbor in tree[node]:
        if neighbor not in visited:
          queue.append(neighbor)  # Add unvisited neighbors to the queue

bfs(tree, 'A')