"""
toposort.py

TODO insert description

"""

from collections import defaultdict


class DictGraph(object):
    """
    A multimap from vertex -> { connected vertices }.
    """

    def __init__(self):
        self.mm = defaultdict(set)

    def add(self, v, w):
        self.mm.get(w) # ensure it exists
        self.mm[v].add(w)


if __name__ == '__main__':
    dg = DictGraph()
    input = [
        (7, 11), (7, 8),
        (5, 11),
        (3, 8), (3, 10),
        (11, 2), (11, 9), (11, 10),
    ]

    [dg.add(v, w) for v, w in input]