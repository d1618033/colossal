import os
import shutil
import sys

import colossal  # noqa
import importlib


def load_example_module(name):
    mod_name = f"colossal.examples.{name}"
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    importlib.invalidate_caches()
    pycache = os.path.join(os.path.dirname(colossal.__file__), 'examples', '__pycache__')
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
    return importlib.import_module(mod_name)
