# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS
        queue, only append last value per level
        proft?
        """

        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            node = None
            for i in range(q_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if node:
                res.append(node.val)

        return res