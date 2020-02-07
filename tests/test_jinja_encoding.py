import pytest
from .utils import load_example_module


@pytest.mark.parametrize("var", ["1"])
def test_if_else(monkeypatch, var):
    monkeypatch.setenv("EXAMPLE_VAR", var)
    mod = load_example_module("ifelse")
    assert mod.x == bool(int(var))


def test_for_loop():
    mod = load_example_module("forloop")
    obj = mod.MyClass(1, 2, 5)
    assert obj.a == 1
    assert obj.b == 2
    assert obj.c == 5
