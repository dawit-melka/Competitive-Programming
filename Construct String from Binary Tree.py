# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        preorder = []
        def dfs(node):
            if not node: return

            preorder.append(str(node.val))
            if node.left or node.right:
                preorder.append("(")
                dfs(node.left)
                preorder.append(")")
            if node.right:
                preorder.append("(")
                dfs(node.right)
                preorder.append(")")

        dfs(root)

        result = "".join(preorder)
        return result
