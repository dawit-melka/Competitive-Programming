# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        even_sum = 0

        def dfs(node):
            if not node:
                return
            
            if node.val % 2 == 0:
                nonlocal even_sum
                if node.left:
                    if node.left.left:
                        even_sum += node.left.left.val
                    if node.left.right:
                        even_sum += node.left.right.val

                if node.right:
                    if node.right.left:
                        even_sum += node.right.left.val
                    if node.right.right:
                        even_sum += node.right.right.val
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return even_sum
