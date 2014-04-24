"""
redblack.py

A left-leaning red-black binary search tree implementation.

Same as BST: get, floor, ceil

Invariant: symmetric order
Invariant: perfect black balance
Invariant: no node has two red links
"""

# TODO check invariant on rotations

from bst import BST, Node


class RedBlack(BST):
    """
    A left-leaning red-black BST.
    """

    def __init__(self, k):
        super(RedBlack, self).__init__(k)
        self.root = Node(k)

    #--------------------------------------------------------------------------
    # Color changes
    #--------------------------------------------------------------------------

    def _color_flip(self, node):
        assert not node.red
        assert node.left.red
        assert node.right.red

        node.red = True
        node.left.red = False
        node.right.red = False

    def _rotate_left(self, node):
        x = node.right
        assert x.red

        node.right = x.left
        x.left = node
        x.red = node.red
        node.red = True
        return x

    def _rotate_right(self, node):
        x = node.left
        assert x.red

        node.left = x.right
        x.right = node
        x.red = node.red
        node.red = True
        return x

    #--------------------------------------------------------------------------
    # Contract checks
    #--------------------------------------------------------------------------

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