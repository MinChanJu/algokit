from collections import deque

def bfs(graph, start):
  visited = set()
  queue = deque([start])
  order = []

  while queue:
    node = queue.popleft()
    if node not in visited:
      order.append(node)
      visited.add(node)
      queue.extend(n for n in graph[node] if n not in visited)

  return order