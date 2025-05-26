# analyzer.py
import ast

def find_algokit_calls(filename):
    with open(filename, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    used_funcs = set()

    class Visitor(ast.NodeVisitor):
        def visit_Call(self, node):
            if isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name) and node.func.value.id == "algokit":
                    used_funcs.add(node.func.attr)
            self.generic_visit(node)

    Visitor().visit(tree)
    return list(used_funcs)