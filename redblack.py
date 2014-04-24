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
        # TODO invariant check
        x = node.right
        assert x.red

        node.right = x.left
        x.left = node
        x.red = node.red
        node.red = True
        return x

    def _has_right_red(self, node=None):
        """
        Returns true if the subtree rooted at node contains a right-leaning
        red link.
        """
        if node is None:
            node = self.root

        return ((node.right and (node.right.red
                                 or self._has_right_red(node.right)))
                or (node.left and self._has_right_red(node.left)))


if __name__ == '__main__':
    pass