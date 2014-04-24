"""
Recursive binary search tree implementation (does not balance on add).
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
    A binary search tree.
    """

    def __init__(self, k):
        self.root = Node(k)

    def _add(self, k, node):
        """
        Adds a key to the tree rooted at node.
        """
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

    #-------------------------------------------------------------------------
    # Public API
    #-------------------------------------------------------------------------

    def add(self, k):
        """
        Adds an entry to the bst instance.
        """
        self._add(k, self.root)

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
        Returns the node with key k.
        """
        return self._get(self.root, k)

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