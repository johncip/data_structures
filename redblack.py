"""
redblack.py

A left-leaning red-black binary search tree implementation.

Same as BST: get, floor, ceil

Invariant: symmetric order
Invariant: perfect black balance
Invariant: no node has two red links
"""

from bst import BST, Node


class RedBlack(BST):
    """
    A left-leaning red-black BST.
    """

    def __init__(self, k):
        super(RedBlack, self).__init__(k)
        self.root = Node(k)

    def _rotate_left(self, node):
        # invariant: symmetric order
        # invariant: perfect black balance
        x = node.right
        assert x.red

        node.right = x.left
        x.left = node.left
        x.red = node.red
        node.red = True
        return x

    # TODO add
    # TODO remove
    # TODO split
    # TODO inorder

if __name__ == '__main__':
    rbt = RedBlack('e')
    rbt.add('a')
    rbt.add('s')
    rbt._get(rbt.root, 's').red = True
    assert rbt._get(rbt.root, 's').red == True
    rbt.add('j')
    rbt.add('z')

    print rbt.level_order()
    rbt.root = rbt._rotate_left(rbt.root)