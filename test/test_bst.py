"""
test_bst.py

Unit tests for BST class.
"""

import random

import pytest

from bst import BST

@pytest.fixture
def bst():
    return BST(keys=[4, 2, 6, 3, 1, 5])


@pytest.fixture
def shuf():
    nums = range(0, 200)
    random.shuffle(nums)
    return BST(keys=nums)


def test_ceil(bst):
    for i in range(1, 7):
        assert bst.ceil(i) == i
    assert bst.ceil(0) == 1
    assert bst.ceil(7) == None


def test_delete_min(bst):
    for i in range(2, 8):
        bst.delete_min()
        assert bst.inorder() == range(i, 7)


def test_delete_no_children(bst):
    for i in [5, 3, 1, 2, 6, 4]:
        bst.delete(i)
    assert bst.inorder() == []


def test_delete_one_child(bst):
    bst.delete(6)
    assert bst.inorder() == [1, 2, 3, 4, 5]
    assert bst.level_order() == "4 \n2 5 \n1 3 "


def test_delete_random(shuf):
    nums = shuf.inorder()
    random.shuffle(nums)
    for i, v in enumerate(nums):
        shuf.delete(v)
        remaining = shuf.inorder()
        assert v not in remaining
        assert len(remaining) == len(nums) - (i + 1)


def test_delete_two_children(bst):
    bst.delete(4)
    assert bst.inorder() == [1, 2, 3, 5, 6]
    bst.delete(5)
    assert bst.inorder() == [1, 2, 3, 6]
    bst.delete(1)
    assert bst.inorder() == [2, 3, 6]


def test_floor(bst):
    for i in range(1, 7):
        assert bst.floor(i) == i
    assert bst.floor(7) == 6
    assert bst.floor(-1) == None


def test_get(bst):
    assert bst._get(bst.root, bst.root.key) is bst.root
    for i in range(1, 7):
        assert bst._get(bst.root, i).key == i


def test_height(bst):
    assert bst.height() == 3


def test_init_empty():
    t = BST()
    assert t.inorder() == []


def test_init_list():
    nums = range(0, 10)
    t = BST(keys=nums)
    assert t.inorder() == nums


def test_inorder():
    nums = range(1, 200)
    random.shuffle(nums)
    bst = BST()
    for n in nums:
        bst.add(n)
    nums.sort()

    assert bst.inorder() == sorted(nums)


def test_level_order(bst):
    assert bst.level_order() == "4 \n2 6 \n1 3 5 "


def test_min(bst):
    assert bst._min(bst.root).key == 1


def test_symmetric_shuffled(shuf):
    assert shuf._symmetric(shuf.root)


def test_symmetric_sorted():
    nums = range(0, 100)
    t = BST(keys=nums)
    assert t._symmetric(t.root)


def test_symmetric_reverse():
    nums = range(199, -1, -1)
    t = BST(keys=nums)
    assert t._symmetric(t.root)


def test_unique_queue():
    BST(keys=[1])
    t = BST(keys=[2])
    assert t.inorder() == [2]