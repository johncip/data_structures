"""
test_redblack.py

Unit tests for red-black tree class.
"""

import pytest

from redblack import RedBlack


@pytest.fixture
def rbt():
    res = RedBlack('e')
    res.add('a')
    res.add('s')
    res.add('j')
    res.add('z')

    return res


@pytest.fixture
def s_node(rbt):
    res = rbt._get(rbt.root, 's')
    assert res.left.key == 'j'
    assert res.right.key == 'z'

    return res


def test_rotate_right(rbt, s_node):
    a_node = rbt._get(rbt.root, 'a')
    a_node.red = True
    rbt.root = rbt._rotate_right(rbt.root)
    assert rbt.root.key == 'a'


def test_rotate_left(rbt, s_node):
    s_node.red = True
    rbt.root = rbt._rotate_left(rbt.root)

    assert s_node.left.key == 'e'
    assert s_node.right.key == 'z'

    e_node = rbt._get(rbt.root, 'e')
    assert e_node.left.key == 'a'
    assert e_node.right.key == 'j'


def test_has_right_red(rbt, s_node):
    assert not rbt._has_right_red()
    s_node.red = True
    assert rbt._has_right_red()

    rbt.root = rbt._rotate_left(rbt.root)
    assert not rbt._has_right_red()

    rbt.root = rbt._rotate_right(rbt.root)
    assert rbt._has_right_red()


def test_symmetric(rbt):
    assert rbt._symmetric()