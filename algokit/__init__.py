import os
import importlib

__all__ = []

module_dir = os.path.dirname(__file__)

for folder in os.listdir(module_dir):
  folder_path = os.path.join(module_dir, folder)

  # 딱 1단계 폴더 + __init__.py 가 있는 경우만 import
  if (
    os.path.isdir(folder_path)
    and os.path.exists(os.path.join(folder_path, "__init__.py"))
    and not folder.startswith("__")
  ):
    try:
      module = importlib.import_module(f".{folder}", package=__name__)
      globals()[folder] = module
      __all__.append(folder)
    except Exception as e:
      print(f"[algokit] Failed to import subpackage: {folder}, error: {e}")