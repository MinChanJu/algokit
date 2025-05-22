from collections import deque

def bfs(graph: dict, start):
  """너비 우선 탐색 (Breadth-First Search, BFS)
  
  start는 graph 안에 존재해야 합니다.

  Args:
    graph (dict): 그래프 딕셔너리 표현
    start (any): 너비 우선 탐색을 시작할 노드 번호

  Returns:
    order (list): 탐색 순서
  
  Raise:
    ValueError: start가 그래프 노드에 없는 경우
  """
  
  if not start in graph:
    raise ValueError("시작 지점이 그래프 노드에 존재해야 합니다.")
  
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