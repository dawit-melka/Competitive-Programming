class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.count = 0
        
        def findKthSmallest(node):
            if node.left:
                findKthSmallest(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            if node.right:
                findKthSmallest(node.right)
        
        findKthSmallest(root)
        return self.result 
