# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, output):
            if not node:
                return None

            # visit the left child
            dfs(node.left, output)
            output.append(node.val)
            # visit the right child
            dfs(node.right, output)

        output = []
        dfs(root, output)
        return output


        

