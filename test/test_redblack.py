"""
test_redblack.py

Unit tests for red-black tree class.
"""

import pytest

from redblack import RedBlack


@pytest.fixture
def rb():
    res = RedBlack(0)
    return res

# def test_rotate_left():
#     rbt = RedBlack('e')
#     rbt.add('a')
#     rbt.add('s').red = True
#     rbt.add('j')
#     rbt.add('z')
#     pass