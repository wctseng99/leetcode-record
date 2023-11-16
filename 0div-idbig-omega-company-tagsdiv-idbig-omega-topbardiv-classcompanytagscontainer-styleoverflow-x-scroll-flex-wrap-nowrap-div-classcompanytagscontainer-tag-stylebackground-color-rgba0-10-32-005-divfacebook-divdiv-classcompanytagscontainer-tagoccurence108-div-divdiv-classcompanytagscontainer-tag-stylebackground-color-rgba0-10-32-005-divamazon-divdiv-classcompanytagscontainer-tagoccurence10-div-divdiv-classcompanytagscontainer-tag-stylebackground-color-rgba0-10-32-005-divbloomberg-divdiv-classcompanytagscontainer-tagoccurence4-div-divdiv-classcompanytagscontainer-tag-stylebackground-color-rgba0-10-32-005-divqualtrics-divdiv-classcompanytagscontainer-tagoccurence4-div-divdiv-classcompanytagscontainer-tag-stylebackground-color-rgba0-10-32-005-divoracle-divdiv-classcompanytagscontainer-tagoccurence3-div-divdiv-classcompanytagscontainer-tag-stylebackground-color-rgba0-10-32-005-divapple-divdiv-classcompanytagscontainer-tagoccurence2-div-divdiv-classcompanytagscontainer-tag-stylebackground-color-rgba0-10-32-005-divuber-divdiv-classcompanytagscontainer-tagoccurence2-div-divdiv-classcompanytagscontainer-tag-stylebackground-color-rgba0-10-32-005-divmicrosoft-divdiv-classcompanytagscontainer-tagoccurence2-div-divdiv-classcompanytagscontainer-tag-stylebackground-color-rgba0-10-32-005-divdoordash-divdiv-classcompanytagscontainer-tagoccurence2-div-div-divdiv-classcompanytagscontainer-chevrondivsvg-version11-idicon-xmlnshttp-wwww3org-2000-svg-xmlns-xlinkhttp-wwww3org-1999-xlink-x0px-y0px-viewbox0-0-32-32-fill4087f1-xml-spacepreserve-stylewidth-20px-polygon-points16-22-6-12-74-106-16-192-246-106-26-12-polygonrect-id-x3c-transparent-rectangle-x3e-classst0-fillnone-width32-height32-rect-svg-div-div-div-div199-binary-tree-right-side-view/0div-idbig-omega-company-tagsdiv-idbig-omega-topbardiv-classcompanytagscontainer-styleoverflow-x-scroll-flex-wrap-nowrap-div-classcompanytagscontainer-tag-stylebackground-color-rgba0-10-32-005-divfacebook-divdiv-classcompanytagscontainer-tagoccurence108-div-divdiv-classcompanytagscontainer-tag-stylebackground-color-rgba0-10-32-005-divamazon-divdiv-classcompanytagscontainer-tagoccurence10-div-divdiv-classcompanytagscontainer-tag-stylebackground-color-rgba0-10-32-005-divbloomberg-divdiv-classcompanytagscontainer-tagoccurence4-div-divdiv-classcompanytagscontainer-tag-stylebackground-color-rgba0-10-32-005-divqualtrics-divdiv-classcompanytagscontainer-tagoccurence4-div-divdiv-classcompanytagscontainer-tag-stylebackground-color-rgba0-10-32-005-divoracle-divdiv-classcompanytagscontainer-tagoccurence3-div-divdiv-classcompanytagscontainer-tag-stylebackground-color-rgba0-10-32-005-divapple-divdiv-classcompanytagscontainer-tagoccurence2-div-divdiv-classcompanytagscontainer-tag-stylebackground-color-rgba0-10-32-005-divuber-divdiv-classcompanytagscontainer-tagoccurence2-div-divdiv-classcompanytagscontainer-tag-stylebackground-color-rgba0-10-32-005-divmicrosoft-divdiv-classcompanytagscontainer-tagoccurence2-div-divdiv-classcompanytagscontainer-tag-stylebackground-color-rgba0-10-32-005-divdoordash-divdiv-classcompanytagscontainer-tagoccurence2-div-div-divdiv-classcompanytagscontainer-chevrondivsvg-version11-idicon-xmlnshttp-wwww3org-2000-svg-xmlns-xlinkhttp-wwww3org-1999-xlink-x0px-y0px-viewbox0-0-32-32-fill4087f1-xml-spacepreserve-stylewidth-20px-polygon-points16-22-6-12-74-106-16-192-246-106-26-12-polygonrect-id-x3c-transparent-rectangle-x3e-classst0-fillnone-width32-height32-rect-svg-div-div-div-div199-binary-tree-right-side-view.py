# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # BFS:level order traversal
        if not root: return []
        queue = deque([root])
        res = []
        
        while queue:
            same_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                same_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if same_level:
                res.append(same_level[-1])
            
        return res
                
            
        