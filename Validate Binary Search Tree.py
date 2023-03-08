class Solution:
    def inOrder(self, node):
        if not node: return []
        left = self.inOrder(node.left)
        right = self.inOrder(node.right)
        return left + [node.val] + right
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inOrder = self.inOrder(root)
        for i in range(1, len(inOrder)):
            if inOrder[i] <= inOrder[i-1]:
                return False
        
        return True

        
