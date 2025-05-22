def dfsStack(graph, start):
  """
  깊이 우선 탐색 (Depth-First Search, DFS) - 스택 기반
  
  start는 graph 안에 존재해야 합니다.

  Args:
    graph (dict): 인접 리스트 형태의 그래프
    start (any): 시작 노드

  Returns:
    order (list): 탐색 순서
  
  Raise:
    ValueError: start가 그래프 노드에 없는 경우
  """
  
  if not start in graph:
    raise ValueError("시작 지점이 그래프 노드에 존재해야 합니다.")
  
  visited = set()
  stack = [start]
  order = []
  
  while stack:
    node = stack.pop()
    if node not in visited:
      order.append(node)
      visited.add(node)
      stack.extend(n for n in graph[node] if n not in visited)

  return order

def dfsRecursive(graph, start, visited=None, order=None):
  """
  깊이 우선 탐색 (Depth-First Search, DFS) - 재귀 기반
  
  start는 graph 안에 존재해야 합니다.

  Args:
    graph (dict): 인접 리스트 형태의 그래프
    start (any): 시작 노드
    visited (set, optional): 방문한 노드 집합 (내부적으로 사용됨)
    order (list, optional): 탐색 순서 (내부적으로 사용됨)

  Returns:
    list: 탐색 순서
    
  Raise:
    ValueError: start가 그래프 노드에 없는 경우
  """
  
  if not start in graph:
    raise ValueError("시작 지점이 그래프 노드에 존재해야 합니다.")
  if visited is None:
    visited = set()
  if order is None:
    order = []

  visited.add(start)
  order.append(start)

  for neighbor in graph[start]:
    if neighbor not in visited:
      dfsRecursive(graph, neighbor, visited, order)

  return order

def dfs(graph, start, mode='stack'):
  """
  깊이 우선 탐색 (Depth-First Search, DFS) - 모드 선택 가능

  Args:
    graph (dict): 인접 리스트 형태의 그래프
    start (any): 시작 노드
    mode (str): 'stack' 또는 'recursive' (기본값: 'stack')

  Returns:
    list: 탐색 순서

  Raises:
    ValueError: start가 그래프에 없거나, mode가 잘못된 경우
  """
  if start not in graph:
    raise ValueError("시작 노드는 그래프에 존재해야 합니다.")
  
  if mode == 'stack':
    return dfsStack(graph, start)
  elif mode == 'recursive':
    return dfsRecursive(graph, start)
  else:
    raise ValueError(f"지원하지 않는 DFS 모드입니다: '{mode}'")
