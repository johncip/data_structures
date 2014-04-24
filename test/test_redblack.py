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


# noinspection PyProtectedMember
def test_rotate_left():
    # TODO implement symetric order check
    # TODO implement no right red link check
    rbt = RedBlack('e')
    e_node = rbt.root
    rbt.add('a')
    rbt.add('s')
    s_node = rbt._get(rbt.root, 's')
    s_node.red = True
    rbt.add('j')
    assert s_node.left.key == 'j'
    rbt.add('z')
    assert s_node.right.key == 'z'

    rbt.root = rbt._rotate_left(rbt.root)
    assert s_node.left.key == 'e'
    assert s_node.right.key == 'z'
    assert e_node.left.key == 'a'
    assert e_node.right.key == 'j'