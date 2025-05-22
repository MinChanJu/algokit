from .dijkstra import dijkstra

class WeightedDirectedGraph:
  """가중치 단방향 그래프 클래스"""

  def __init__(self, nodes: set):
    """
    WeightedDirectedGraph를 초기화합니다.

    node 이름에 대한 규칙은 없으며 다양한 값이 가능합니다.
    
    단, nodes 안의 요소는 immutable(불변) 타입이어야 합니다.

    인접 리스트는 (이웃 노드, 가중치) 튜플로 구성됩니다.

    Args:
      nodes (set): 노드들의 집합
    """
    self.graph = {node: [] for node in nodes}
    self.nodes = nodes
    self.N = len(nodes)

  def add(self, u, v, weight: int|float):
    """
    가중치 단방향 간선을 추가합니다. (u → v, 가중치 w)
    
    두 정점 u, v는 모두 WeightedDirectedGraph.nodes 안에 존재해야 합니다.

    Args:
      u (any): 출발 정점
      v (any): 도착 정점
      weight (int | float): 간선의 가중치

    Raises:
      ValueError: u 또는 v가 그래프 노드에 없는 경우
    """
    if u not in self.nodes or v not in self.nodes:
      raise ValueError("두 정점이 모두 그래프 노드에 존재해야 합니다.")

    self.graph[u].append((v, weight))

  def dijkstra(self, start):
    """WeightedDirectedGraph에서 다익스트라 알고리즘 실행"""
    return dijkstra(self.graph, start)