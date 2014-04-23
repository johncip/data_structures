"""
Binary tree stuff.
"""


class Node:
    """
    A binary tree node.
    """
    key = None
    left = None
    right = None

    def __init__(self, k):
        self.key = k

    def __str__(self):
        return str(self.key)


class BST:
    """
    An unbalanced binary tree.
    """

    def __init__(self, k):
        self.root = Node(k)

    def add(self, k):
        """
        Adds an entry to the binary tree.
        """
        self._add(k, self.root)

    def _add(self, k, node):
        if not node:
            return Node(k)
        if k < node.key:
            node.left = self._add(k, node.left)
            return node
        elif k > node.key:
            node.right = self._add(k, node.right)
            return node
        else:  # k == node.key
            return node

    def inorder(self):
        """
        in-order traversal
        """
        return self._inorder(self.root, [])

    def _inorder(self, node, q):
        if node:
            self._inorder(node.left, q)
            q.append(node.key)
            self._inorder(node.right, q)

        return q

    def _print_level(self, node, level):
        if not node:
            return
        if level == 1:
            print node.key,
        else:
            self._print_level(node.left, level - 1)
            self._print_level(node.right, level - 1)

    def level_order(self):
        """
        Level-order print.
        """
        height = self._height(self.root)
        for level in range(1, height + 1):
            self._print_level(self.root, level)
            print

    def height(self):
        """
        Returns the max height of the binary tree instance.
        """
        return self._height(self.root)

    def _height(self, node):
        """
        Returns the max height of the tree rooted at node.
        """
        if not node:
            return 0

        return 1 + max(self._height(node.left),
                       self._height(node.right))

    def floor(self, k):
        """
        Returns the largest key smaller than k.
        """
        return self._floor(self.root, k)

    def _floor(self, node, k):
        # search key is smaller: keep going left
        # search key is larger: floor(right) if one exists, else self
        if not node:
            return None
        elif k == node.key:
            return k
        elif k < node.key:
            return self._floor(node.left, k)
        elif k > node.key:
            rf = self._floor(node.right, k)
            return rf if rf else node.key

    def ceil(self, k):
        """
        Returns the smallest key larger than k.
        """
        return self._ceil(self.root, k)

    def _ceil(self, node, k):
        # search key is larger: keep going right
        # search key is smaller: floor(left) if one exists, else self
        if not node:
            return None

        if k > node.key:
            return self._ceil(node.right, k)
        elif k < node.key:
            lf = self._ceil(node.left, k)
            return lf if lf else node.key
        else:  # k == node.key
            return k

    def get(self, k):
        """
        Returns the node with key k.
        """
        return self._get(self.root, k)

    def _get(self, node, k):
        if not node:
            return None

        if k < node.key:
            return self._get(node.left, k)
        elif k > node.key:
            return self._get(node.right, k)
        else:  # k == node.key
            return node

    def delete_min(self):
        """
        Delete the minimum element.
        """
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        if not node.left:
            return node.right

        node.left = self._delete_min(node.left)
        return node

    def parent(self, k):
        """
        Returns parent of node with value k.
        """
        assert self.get(k)
        if self.get(k) == self.root:
            return None
        return self._parent(self.root, k)

    def _parent(self, node, k):
        if not node:
            return None
        if node.left.key == k or node.right.key == k:
            return node
        else:
            return self._parent(node.left, k) or self._parent(node.right, k)

    def delete(self, k):
        """
        Recursive delete.
        """
        self.root = self._delete(self.root, k)

    def _delete(self, node, k):
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

        return node