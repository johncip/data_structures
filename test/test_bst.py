"""
test_bst.py

Unit tests for BST class.
"""

import random

import pytest

from bst import BST


@pytest.fixture
def bst():
    res = BST(4)
    [res.add(e) for e in [2, 6, 3, 1, 5]]
    return res


def test_inorder():
    nums = range(1, 100)
    random.shuffle(nums)
    t = BST(nums[0])
    for n in nums[1:]:
        t.add(n)
    nums.sort()

    assert t.inorder() == sorted(nums)


def test_unique_queue():
    BST(1)
    assert BST(2).inorder() == [2]


def test_floor(bst):
    for i in range(1, 7):
        assert bst.floor(i) == i
    assert bst.floor(7) == 6
    assert bst.floor(-1) is None


def test_ceil(bst):
    for i in range(1, 7):
        assert bst.ceil(i) == i
    assert bst.ceil(0) == 1
    assert bst.ceil(7) is None


def test_get(bst):
    assert bst._get(bst.root, bst.root.key) is bst.root
    for i in range(1, 7):
        assert bst._get(bst.root, i).key == i


def test_height(bst):
    assert bst.height() == 3


def test_delete_min(bst):
    for i in range(2, 8):
        bst.delete_min()
        assert bst.inorder() == range(i, 7)


def test_level_order(bst):
    assert bst.level_order() == "4 \n2 6 \n1 3 5 "


def test_delete_leaf(bst):
    for i in [5, 3, 1, 2, 6, 4]:
        bst.delete(i)
    assert bst.inorder() == []


def test_delete_one_child(bst):
    bst.delete(6)
    assert bst.inorder() == [1, 2, 3, 4, 5]
    assert bst.level_order() == "4 \n2 5 \n1 3 "


def test_min(bst):
    assert bst._min(bst.root).key == 1


def test_delete_two_children(bst):
    bst.delete(4)
    assert bst.inorder() == [1, 2, 3, 5, 6]
    bst.delete(5)
    assert bst.inorder() == [1, 2, 3, 6]
    bst.delete(1)
    assert bst.inorder() == [2, 3, 6]


def test_delete_random():
    maxx = 200
    nums = range(0, maxx)
    random.shuffle(nums)
    t = BST(nums[0])
    [t.add(i) for i in nums[1:]]

    random.shuffle(nums)
    for i, v in enumerate(nums):
        t.delete(v)
        remaining = t.inorder()
        assert v not in remaining
        assert len(remaining) == maxx - (i + 1)