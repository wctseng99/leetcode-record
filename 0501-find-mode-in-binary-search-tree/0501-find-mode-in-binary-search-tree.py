# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        freq = defaultdict(int)

        # bfs
        def dfs(node):
            if not node: return None
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        max_freq = max(freq.values())
        return [key for key, val in freq.items() if val == max_freq]