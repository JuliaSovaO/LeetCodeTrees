"""
Delete Node in a BST
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp = root.right
            while temp.left is not None:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root


# Test 1
# root = [5, 3, 6, 2, 4, None, 7]
# key = 3
# [5,4,6,2,None,None,7]

root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(6)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(None)
root1.right.right = TreeNode(7)

sol = Solution()
res1 = sol.deleteNode(root1, 3)

print(
    [
        res1.val,
        res1.left.val,
        res1.right.val,
        res1.left.left.val,
        res1.left.right.val if res1.left.right else None,
        res1.right.left.val,
        res1.right.right.val,
    ]
)

# Test 2
# root = [5, 3, 6, 2, 4, None, 7]
# key = 0
# [5,3,6,2,4,None,7]

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(None)
root2.right.right = TreeNode(7)

res2 = sol.deleteNode(root2, 0)
print(
    [
        res2.val,
        res2.left.val,
        res2.right.val,
        res2.left.left.val,
        res2.left.right.val,
        res2.right.left.val,
        res2.right.right.val,
    ]
)

# Test 3
# root = []
# key = 0
# []

res3 = sol.deleteNode(None, 0)
print(res3 if res3 else [])
