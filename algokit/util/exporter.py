import inspect
import importlib
from typing import List
from .analyzer import analyze_used_symbols

def extract_function_source(func):
    return inspect.getsource(func)

def resolve_func_module(func_path: str):
    """
    'graph.dijkstra' -> ('algokit.graph', 'dijkstra')
    """
    parts = func_path.split('.')
    module_path = '.'.join(['algokit'] + parts[:-1])
    func_name = parts[-1]
    return module_path, func_name

def export_used_functions(dest_file: str, used_funcs: List[str], output_path: str):
    """
    used_funcs 예: ['graph.dijkstra', 'list.upper_bound']
    """
    function_sources = []

    for func_path in used_funcs:
        module_path, func_name = resolve_func_module(func_path)

        try:
            module = importlib.import_module(module_path)
        except ImportError:
            raise ValueError(f"모듈 {module_path} 을(를) import할 수 없습니다.")

        if not hasattr(module, func_name):
            raise ValueError(f"함수 {func_name} 이(가) {module_path} 에 존재하지 않습니다.")

        func = getattr(module, func_name)
        source = extract_function_source(func)
        function_sources.append(source)

    with open(dest_file, "r", encoding="utf-8") as f:
        original_code = f.read()

    combined_code = "\n\n".join(function_sources) + "\n\n" + original_code

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(combined_code)

    print(f"✅ '{output_path}' 파일로 제출 코드가 생성되었습니다.")
    
def exporter(main_file: str, output_file: str):
  used_funcs = analyze_used_symbols(main_file)
  export_used_functions(dest_file=main_file, used_funcs=used_funcs, output_path=output_file)