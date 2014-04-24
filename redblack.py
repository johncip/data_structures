"""
redblack.py

A left-leaning red-black tree implementation.
Based on Sedgewick's recursive implementation strategy.

Invariant: symmetric order
Invariant: perfect black balance
Invariant: no node has two red links
"""

from bst import BST, Node


# TODO implement delete

def red(node):
    """
    Returns true if a node *exists* and has a red link.
    """
    return node and node.red


class RedBlack(BST):
    """
    A left-leaning red-black BST.
    """

    #--------------------------------------------------------------------------
    # Balancing
    #--------------------------------------------------------------------------

    def _balance(self, node):
        """
        Balance a node's local links.
        """
        if red(node.right) and not red(node.left):
            node = self._rotate_left(node)
        if red(node.left) and red(node.left.left):
            node = self._rotate_right(node)
        if red(node.left) and red(node.right):
            self._flip_color(node)

        return node

    def _flip_color(self, node):
        """
        Recolor to split a 4-node.
        """
        # assert not node.red
        assert node.left.red
        assert node.right.red

        if node is not self.root:
            node.red = True

        node.left.red = False
        node.right.red = False

    def _rotate_left(self, node):
        """
        Rotate a right-leaning red link to lean left.
        """
        x = node.right
        assert x.red

        # swap node with right child.
        node.right = x.left
        x.left = node
        x.red = node.red
        node.red = True
        return x

    def _rotate_right(self, node):
        """
        Rotate a left-leaning red link to lean right.
        """
        x = node.left
        assert x.red

        # swap node with left child
        node.left = x.right
        x.right = node
        x.red = node.red
        node.red = True
        return x

    #--------------------------------------------------------------------------
    # Implementations
    #--------------------------------------------------------------------------

    def _add(self, node, k):
        """
        Adds a node with key k to the subtree rooted at node, preserving
        black balance.
        """
        if not node:
            return Node(k, red=True)

        if k < node.key:
            node.left = self._add(node.left, k)
        elif k > node.key:
            node.right = self._add(node.right, k)

        return self._balance(node)

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
    nums = range(0, 127)

    t = RedBlack(keys=nums)
    import math

    print "height: ", t._height(t.root)
    print "log(len(nums)): ", math.log(len(nums), 2)