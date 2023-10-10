# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', px: 'TreeNode', qx: 'TreeNode') -> 'TreeNode':
        result = None

        def dfs(node, foundP, foundQ):
            nonlocal result
            if not node or result:
                return (foundP, foundQ)

            (lp, lq) = dfs( node.left, foundP , foundQ )
            (rp, rq) = dfs( node.right, foundP, foundQ )

            hasP = any([lp, (node == px), rp])
            hasQ = any([lq, (node == qx), rq])
            
            if hasP and hasQ and result == None:
                result = node
            
            return (hasP, hasQ)
            
        dfs(root, False, False)
        return result
        
