# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # check if the tree empyty
        if not root:
            return []

        # init the queue
        queue = deque([root])
        levels = [[root.val]]

        # BFS traversal
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                    temp.append(node.left.val)
                if node.right: 
                    queue.append(node.right)
                    temp.append(node.right.val)
            if temp:
                levels.append(temp)
    
        return levels


