# algokit

Python 라이브러리 for 다양한 알고리즘.

## 사용법

```bash
pip install git+https://github.com/MinChanJu/algokit.git
```

```python
from algokit.graph import bfs
from algokit.sort import quicksort

graph = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
print(bfs(graph, 'A'))

arr = [3, 1, 4, 1, 5]
print(quicksort(arr))
```