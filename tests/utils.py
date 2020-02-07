import colossal  # noqa
import importlib


def load_example_module(name):
    return importlib.reload(importlib.import_module(f"colossal.examples.{name}"))
