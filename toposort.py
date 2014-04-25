"""
toposort.py

TODO insert description

"""

from collections import defaultdict


def adjacent(edges):
    """
    Given [edges], returns a map: node -> {connected nodes}.
    """
    res = defaultdict(set)

    for v, w in edges:
        res[v].add(w)
        _ = res[w]

    return res


def toposort(graph):
    """
    Returns a topological sort using DFS method.

    @param graph    a map from node -> {connected nodes}
    """
    nodes = set(graph.keys())
    marked = set()
    temp = set()
    res = []

    def visit(n):
        assert n not in temp, "must be acyclic"

        if n not in marked:
            temp.add(n)
            for m in graph[n]:
                visit(m)
            marked.add(n)
            res.append(n)
            temp.remove(n)

    while marked < nodes:
        unmarked = iter(nodes - marked)
        visit(next(unmarked))

    return res[::-1]


if __name__ == '__main__':
    G = adjacent([
        (7, 11), (7, 8),
        (5, 11),
        (8, 9),
        (3, 8), (3, 10),
        (11, 2), (11, 9), (11, 10)])
    print G
    print toposort(G)

    K = adjacent([
        ('keep', 'on'),
        ('keep', 'calm'),
        ('calm', 'and'),
        ('calm', 'carry'),
        ('carry', 'on'),
    ])
    print K
    print toposort(K)