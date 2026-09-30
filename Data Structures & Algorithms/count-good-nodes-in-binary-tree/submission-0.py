# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS via recursion
        on path to node, pass down max(parent_nodes val)
        if val > max, we're good
        append to global res list
        """
        if not root:
            return 0

        count = 0

        def dfs(node: Optional[TreeNode], prev_max: int):
            nonlocal count
            if not node:
                return
            if node.val >= prev_max:
                count += 1
                prev_max = node.val
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)

        dfs(root, root.val)
        return count
