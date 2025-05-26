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
    module_path = '.'.join(parts[:-1])
    func_name = parts[-1]
    return module_path, func_name

def export_used_symbols(dest_file: str, used_symbols: List[str], output_path: str):
    sources = []

    for symbol_path in used_symbols:
        module_path, symbol_name = resolve_func_module(symbol_path)

        try:
            module = importlib.import_module(module_path)
        except ImportError:
            raise ImportError(f"❌ 모듈 {module_path} 을(를) import할 수 없습니다.")

        if not hasattr(module, symbol_name):
            raise AttributeError(f"❌ '{symbol_name}' 이(가) {module_path} 에 존재하지 않습니다.")

        symbol = getattr(module, symbol_name)

        # ✅ 실제 정의된 모듈로 다시 추적
        real_module_path = symbol.__module__
        real_module = importlib.import_module(real_module_path)
        real_symbol = getattr(real_module, symbol_name)

        try:
            source = inspect.getsource(real_symbol)
            sources.append(source)
        except TypeError:
            raise TypeError(f"❌ '{symbol_path}'는 소스를 추출할 수 없습니다.")

    with open(dest_file, "r", encoding="utf-8") as f:
        original_code = f.read()

    combined_code = "\n\n".join(sources) + "\n\n" + original_code

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(combined_code)

    print(f"✅ '{output_path}' 파일로 제출 코드가 생성되었습니다.")
    
def exporter(main_file: str, output_file: str):
  used_funcs = analyze_used_symbols(main_file)
  export_used_symbols(dest_file=main_file, used_funcs=used_funcs, output_path=output_file)