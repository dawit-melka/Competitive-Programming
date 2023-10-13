# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.min_moves = 0
        
        def traverse(node):
            if not node:
                return (0, 0)
            l_nodes, l_coins = traverse(node.left)
            r_nodes, r_coins = traverse(node.right)
            l_diff = abs(l_coins - l_nodes)
            r_diff = abs(r_coins - r_nodes)
            self.min_moves += (l_diff + r_diff)
            return (1+l_nodes+r_nodes, node.val+l_coins+r_coins)
        
        traverse(root)

        return self.min_moves
        
