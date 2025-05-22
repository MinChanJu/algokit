import os
import importlib

__all__ = []

module_dir = os.path.dirname(__file__)

for filename in os.listdir(module_dir):
  if filename.endswith(".py") and filename != "__init__.py":
    modulename = filename[:-3]
    module = importlib.import_module(f".{modulename}", package=__name__)
    globals().update(vars(module))
    __all__.append(modulename)