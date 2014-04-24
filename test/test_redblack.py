"""
test_redblack.py

Unit tests for red-black tree class.
"""

import pytest

from redblack import RedBlack


@pytest.fixture
def rbt():
    return RedBlack(keys='easjz')


@pytest.fixture
def s_node(rbt):
    res = rbt._get(rbt.root, 's')

    return res


def test_has_right_red(rbt, s_node):
    assert not rbt._has_right_red()
    rbt.root.right.red = True
    assert rbt._has_right_red()

    rbt.root = rbt._rotate_left(rbt.root)
    assert not rbt._has_right_red()

    rbt.root = rbt._rotate_right(rbt.root)
    assert rbt._has_right_red()


def test_rotate_left(rbt, s_node):
    root = rbt.root
    right = root.right
    right.red = True

    rbt.root = rbt._rotate_left(root)
    assert right is rbt.root
    assert root is rbt.root.left

    pass


def test_rotate_right(rbt, s_node):
    root = rbt.root
    left = root.left
    left.red = True

    rbt.root = rbt._rotate_right(root)
    assert left is rbt.root
    assert root is rbt.root.right


def test_flip_color(rbt):
    root = rbt.root
    root.left.red = True
    root.right.red = True
    rbt._flip_color(root)
    assert not root.left.red
    assert not root.right.red


def test_symmetric(rbt):
    assert rbt._symmetric()