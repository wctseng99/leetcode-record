# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # bfs
        queue = deque([[1, root]])
        res = 0
        while queue:
            res = max(res, queue[-1][0] - queue[0][0] + 1)
            for _ in range(len(queue)):
                index, node = queue.popleft()
                if node.left:
                    queue.append([index * 2, node.left])
                if node.right:
                    queue.append([index * 2 + 1, node.right])

        return res