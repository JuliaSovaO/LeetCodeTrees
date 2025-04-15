"""
Sort binary tree by levels
"""

from collections import deque


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if not node:
        return []

    result = []
    queue = deque([node])

    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


assert tree_by_levels(None) == []
root = Node(
    Node(None, Node(None, None, 4), 2),
    Node(Node(None, None, 5), Node(None, None, 6), 3),
    1,
)
assert tree_by_levels(root) == [1, 2, 3, 4, 5, 6]
tree = Node(
    Node(Node(None, None, 1), Node(None, None, 3), 8),
    Node(Node(None, None, 4), Node(None, None, 5), 9),
    2,
)
assert tree_by_levels(tree) == [2, 8, 9, 1, 3, 4, 5]
tree2 = Node(
    Node(None, Node(None, None, 3), 8),
    Node(None, Node(None, Node(None, None, 7), 5), 4),
    1,
)
assert tree_by_levels(tree2) == [1, 8, 4, 3, 5, 7]
