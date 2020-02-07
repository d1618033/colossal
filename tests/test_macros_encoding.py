import pytest
import textwrap
from colossal.macros_encoding import decode
from .utils import load_example_module


def test_dict_macro():
    mod = load_example_module("dict_macro")
    assert mod.w == dict(x=1, y=2, z=3)


def test_macro():
    decoded, _ = decode(textwrap.dedent("""
        x = 1
        y = 2
        z = 3
        dict@(x,y,z)
        """
    ).encode())
    assert decoded.strip() == textwrap.dedent("""
        x = 1
        y = 2
        z = 3
        dict(x=x, y=y, z=z)
        """
    ).strip()

