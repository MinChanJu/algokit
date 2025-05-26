# analyzer_advanced.py
import ast

class AliasTracker(ast.NodeVisitor):
    def __init__(self):
        self.aliases = {}  # {'ak': 'algokit'}

    def visit_Import(self, node):
        for alias in node.names:
            if alias.asname:
                self.aliases[alias.asname] = alias.name

    def visit_ImportFrom(self, node):
        pass  # 생략 가능

class AlgokitUsageFinder(ast.NodeVisitor):
    def __init__(self, aliases):
        self.aliases = aliases
        self.used_symbols = set()

    def visit_Attribute(self, node):
        # 예: ak.graph.WeightedDirectedGraph
        full_attr = []
        curr = node
        while isinstance(curr, ast.Attribute):
            full_attr.append(curr.attr)
            curr = curr.value
        if isinstance(curr, ast.Name) and curr.id in self.aliases:
            full_attr.append(self.aliases[curr.id])
            full_attr.reverse()
            dotted_path = ".".join(full_attr)
            if dotted_path.startswith("algokit."):
                self.used_symbols.add(dotted_path)
        self.generic_visit(node)

def analyze_used_symbols(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    alias_tracker = AliasTracker()
    alias_tracker.visit(tree)

    usage_finder = AlgokitUsageFinder(alias_tracker.aliases)
    usage_finder.visit(tree)

    return usage_finder.used_symbols