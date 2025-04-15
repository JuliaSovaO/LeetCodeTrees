"""
Binary Tree Traversal
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(node):
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)


def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)


def post_order(node):
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.left = b
a.right = c
c.left = d

assert pre_order(a) == ["A", "B", "C", "D"]
assert in_order(a) == ["B", "A", "D", "C"]
assert post_order(a) == ["B", "D", "C", "A"]

assert pre_order(b) == ["B"]
assert in_order(b) == ["B"]
assert post_order(b) == ["B"]

assert pre_order(None) == []
assert in_order(None) == []
assert post_order(None) == []
