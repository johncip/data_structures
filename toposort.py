"""
toposort.py

Topological sort using DFS method.

"""

from collections import defaultdict


def adjacency_list(edges):
    """
    Given ["v,w"], returns a map: node -> {connected nodes}.
    """
    res = defaultdict(list)

    for edge in edges:
        v, w = edge.split(',')
        res[v].append(w)

    return res


def topological_sort(deps):
    """
    Returns a topological sort.
    """
    graph = adjacency_list(deps)
    nodes = graph.keys()

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

    for n in nodes:
        visit(n)

    return res[::-1]


if __name__ == '__main__':
    deps = ['7,11', '7,8', '5,11', '8,9', '3,8', '3,10', '11,2', '11,9',
            '11,10']
    print topological_sort(deps)

    deps = ["keep,on", "keep,calm", "calm,and", "calm,carry", "carry,on"]
    print topological_sort(deps)