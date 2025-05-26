# analyzer_advanced.py
import ast

class AliasTracker(ast.NodeVisitor):
    def __init__(self):
        self.aliases = {}  # 예: {'ak': 'algokit'}

    def visit_Import(self, node):
        for alias in node.names:
            if alias.asname:
                self.aliases[alias.asname] = alias.name
            else:
                self.aliases[alias.name] = alias.name  # import algokit 형태도 처리

    def visit_ImportFrom(self, node):
        pass  # 현재는 사용 안함

class AlgokitUsageFinder(ast.NodeVisitor):
    def __init__(self, aliases):
        self.aliases = aliases
        self.used_symbols = set()

    def get_full_attribute_path(self, node):
        names = []
        while isinstance(node, ast.Attribute):
            names.append(node.attr)
            node = node.value
        if isinstance(node, ast.Name):
            base = self.aliases.get(node.id, node.id)
            names.append(base)
            names.reverse()
            return ".".join(names)
        return None

    def visit_Call(self, node):
        # 클래스 생성자 호출도 포함
        path = self.get_full_attribute_path(node.func)
        if path and path.startswith("algokit."):
            self.used_symbols.add(path)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        # 객체.method → 해당 객체가 algokit에서 왔는지 모를 수 있음
        path = self.get_full_attribute_path(node)
        if path and path.startswith("algokit."):
            self.used_symbols.add(path)
        self.generic_visit(node)

def analyze_used_symbols(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    alias_tracker = AliasTracker()
    alias_tracker.visit(tree)

    usage_finder = AlgokitUsageFinder(alias_tracker.aliases)
    usage_finder.visit(tree)

    return usage_finder.used_symbols