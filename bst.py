"""
bst.py

Recursive binary search tree implementation.
"""


class Node(object):
    """
    A binary tree node.
    """

    left = None
    right = None
    value = None
    red = False  # color of parent link

    def __init__(self, k):
        self.key = k

    def __str__(self):
        return str(self.key)


class BST(object):
    """
    A binary search tree.
    """

    def __init__(self, k):
        """
        Creates a new BST with root containing key k.
        """
        self.root = Node(k)

    def __str__(self):
        return self.level_order()

    #-------------------------------------------------------------------------
    # Implementations
    #-------------------------------------------------------------------------

    def _add(self, node, k):
        """
        Adds a node with key k to the subtree rooted at node.
        Note: returns parent if parent exists, else new node.
        """
        if not node:
            return Node(k)
        if k < node.key:
            node.left = self._add(node.left, k)
            return node
        elif k > node.key:
            node.right = self._add(node.right, k)
            return node
        else:  # k == node.key
            return node

    def _ceil(self, node, k):
        """
        Returns the smallest key larger than k from the subtree rooted at node.
        """
        if not node:
            return None

        if k > node.key:
            # key is larger: continue right
            return self._ceil(node.right, k)
        elif k < node.key:
            # key is smaller: floor(left) if one exists, else cur
            lf = self._ceil(node.left, k)
            return lf if lf else node.key
        else:  # k == node.key
            return k

    def _delete(self, node, k):
        """
        Deletes a key from the subtree rooted at node.
        """
        if not node:
            return None

        if k < node.key:
            node.left = self._delete(node.left, k)
        elif k > node.key:
            node.right = self._delete(node.right, k)
        else:
            # zero children
            if not (node.left or node.right):
                return None

            # one child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # two children
            succ = self._min(node.right)
            succ.right = self._delete_min(node.right)
            succ.left = node.left
            return succ

        return node

    def _delete_min(self, node):
        """
        Deletes the smallest key from the subtree rooted at node.
        """
        if not node.left:
            return node.right

        node.left = self._delete_min(node.left)
        return node

    def _floor(self, node, k):
        """
        Returns the largest key smaller than k from the subtree rooted at node.
        """
        if not node:
            return None
        elif k == node.key:
            return k
        elif k < node.key:
            # key is smaller: continue left
            return self._floor(node.left, k)
        elif k > node.key:
            # key is larger: floor(right) if one exists, else current
            rf = self._floor(node.right, k)
            return rf if rf else node.key

    def _get(self, node, k):
        """
        Returns the node with key k from the subtree rooted at node.
        """
        if not node:
            return None

        if k < node.key:
            return self._get(node.left, k)
        elif k > node.key:
            return self._get(node.right, k)
        else:  # k == node.key
            return node

    def _height(self, node):
        """
        Returns the max height of the tree rooted at node.
        """
        if not node:
            return 0

        return 1 + max(self._height(node.left), self._height(node.right))

    def _inorder(self, node, q):
        """
        Recursive in-order traversal.
        """
        if node:
            self._inorder(node.left, q)
            q.append(node.key)
            self._inorder(node.right, q)

        return q

    def _min(self, node):
        """
        Returns the node containing the smallest key.
        """
        if not node:
            return None

        return self._min(node.left) or node

    def _print_level(self, node, level):
        if not node:
            return ""
        if level == 1:
            return str(node.key) + " "
        else:
            left = self._print_level(node.left, level - 1)
            right = self._print_level(node.right, level - 1)
            return str(left) + str(right)

    def _symmetric(self, node=None):
        """
        Returns true if the subtree rooted at node is in symmetric order.
        """
        if node is None:
            node = self.root

        left_sym = (not node.left
                    or (node.key > node.left.key
                        and self._symmetric(node.left)))

        def right_sym():  # for delayed evaluation
            return (not node.right
                    or (node.key < node.right.key
                        and self._symmetric(node.right)))

        return left_sym and right_sym()

    #-------------------------------------------------------------------------
    # Public API
    #-------------------------------------------------------------------------

    def add(self, k):
        """
        Adds an entry to the bst instance and returns the node.
        """
        return self._add(self.root, k)

    def ceil(self, k):
        """
        Returns the smallest key larger than k.
        """
        return self._ceil(self.root, k)

    def delete(self, k):
        """
        Deletes a key k.
        """
        self.root = self._delete(self.root, k)

    def delete_min(self):
        """
        Delete the minimum key.
        """
        self.root = self._delete_min(self.root)

    def floor(self, k):
        """
        Returns the largest key smaller than k.
        """
        return self._floor(self.root, k)

    def get(self, k):
        """
        Returns the value at key k.
        """
        return self._get(self.root, k).value

    def height(self):
        """
        Returns the max height.
        """
        return self._height(self.root)

    def inorder(self):
        """
        in-order traversal
        """
        return self._inorder(self.root, [])

    def level_order(self):
        """
        Level-order traversal (returns string).
        """
        maxh = self._height(self.root) + 1
        levels = [self._print_level(self.root, level) for level in range(1, maxh)]
        return "\n".join(levels)


if __name__ == "__main__":
    import random

    nums = range(0, 100)
    random.shuffle(nums)
    bst = BST(nums[0])
    [bst.add(i) for i in nums[1:]]
    print bst.level_order()