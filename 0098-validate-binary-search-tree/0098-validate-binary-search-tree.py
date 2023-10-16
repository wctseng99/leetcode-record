# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # using inorder travelsal to check
        def inOrder(node, lower = -float('inf'), upper = float('inf')):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False

            # check left subtree and right subtree respectively.
            return inOrder(node.left, lower, node.val) and inOrder(node.right, node.val, upper)

        return inOrder(root)