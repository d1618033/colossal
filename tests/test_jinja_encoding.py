import pytest
import importlib
import colossal.jinja_encoding  # noqa


def _load_example_module(name):
    return importlib.reload(importlib.import_module(f"colossal.examples.{name}"))


@pytest.mark.parametrize("var", ["1"])
def test_if_else(monkeypatch, var):
    monkeypatch.setenv("EXAMPLE_VAR", var)
    mod = _load_example_module("ifelse")
    assert mod.x == bool(int(var))


@pytest.mark.parametrize("var", ["1"])
def test_for_loop(monkeypatch, var):
    monkeypatch.setenv("EXAMPLE_VAR", var)
    mod = _load_example_module("forloop")
    obj = mod.MyClass(1, 2, 5)
    assert obj.a == 1
    assert obj.b == 2
    assert obj.c == 5
