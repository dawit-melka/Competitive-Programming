# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, _min, _max):
        if not node:
            return True
        if node.val <= _min or node.val >= _max:
            return False
        valid_left = self.helper(node.left, _min, node.val)
        valid_right = self.helper(node.right, node.val, _max)

        return valid_left and valid_right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
        
