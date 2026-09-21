# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node: Optional[TreeNode]):
            if not node:
                return
            recurse(node.right)
            recurse(node.left)
            tmp = node.left
            node.left = node.right
            node.right = tmp
        recurse(root)
        return root
