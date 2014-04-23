import pytest

from bst import BST


@pytest.fixture
def bst():
    bst = BST(4)
    [bst.add(e) for e in [2, 6, 3, 1, 5]]
    return bst


def test_inorder(bst):
    assert bst.inorder() == range(1, 7)


def test_unique_queue(bst):
    BST(1)
    assert BST(2).inorder() == [2]


def test_floor(bst):
    for i in range(1, 7):
        assert bst.floor(i) == i
    assert bst.floor(7) == 6
    assert bst.floor(-1) == None


def test_ceil(bst):
    for i in range(1, 7):
        assert bst.ceil(i) == i
    assert bst.ceil(0) == 1
    assert bst.ceil(7) == None


def test_get(bst):
    assert bst.get(4) is bst.root
    for i in range(1, 7):
        assert bst.get(i).key == i


def test_parent(bst):
    assert bst.parent(bst.root.key) is None
    assert bst.parent(2) is bst.get(4)
    assert bst.parent(6) is bst.get(4)
    assert bst.parent(1) is bst.get(2)


def test_height(bst):
    assert bst.height() == 3


def test_delete_min(bst):
    for i in range(2, 8):
        bst.delete_min()
        assert bst.inorder() == range(i, 7)


def test_level_order(bst):
    assert bst.level_order() == "4 \n2 6 \n1 3 5 "


def test_delete(bst):
    for i in [5, 3, 1, 2, 6, 4]:
        bst.delete(i)
    assert bst.inorder() == []