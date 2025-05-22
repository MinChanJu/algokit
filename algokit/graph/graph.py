from .bfs import bfs  # ✅ 불러오기

class Graph:
  """양방향 그래프 클래스"""

  def __init__(self, nodes: set):
    """
    Graph를 초기화하는 생성자입니다.

    node 이름에 대한 규칙은 없으며 다양한 값이 가능합니다.
    
    단, nodes 안의 요소는 immutable(불변) 타입이어야 합니다.

    Args:
      nodes (set): 노드의 이름이 담긴 집합
    """
    self.graph = {node: [] for node in nodes}
    self.nodes = nodes
    self.N = len(nodes)

  def add(self, u, v):
    """
    양방향 간선을 추가합니다. (u ←→ v)
    
    두 정점 u, v는 모두 DirectedGraph.nodes 안에 존재해야 합니다.

    Args:
      u (any): 하나의 정점
      v (any): 하나의 정점

    Raises:
      ValueError: u 또는 v가 그래프 노드에 없는 경우
    """
    if u not in self.nodes or v not in self.nodes:
        raise ValueError("두 정점이 모두 그래프 노드에 존재해야 합니다.")

    self.graph[u].append(v)
    self.graph[v].append(u)
    
  def bfs(self, start):
    """너비 우선 탐색 (Breadth-First Search, BFS)

    Args:
      graph (dict): 그래프 딕셔너리 표현
      N (int): 전체 노드의 수
      start (any): 너비 우선 탐색을 시작할 노드 번호

    Returns:
      order (list): 탐색 순서
    """
    return bfs(self.graph, start)  # ✅ 모듈 함수 재사용