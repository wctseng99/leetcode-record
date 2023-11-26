# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        # bfs
        queue = deque([root])
        
        while queue:
            level_vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_vals.append(None)

            left, right = 0, len(level_vals)-1
            while left < right:
                if level_vals[left] != level_vals[right]:
                    return False
                left += 1
                right -= 1

        return True