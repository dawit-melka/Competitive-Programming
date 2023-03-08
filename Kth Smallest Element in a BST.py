class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = -1
        self.count = k
    
        def helper(node):
            if node.left: helper(node.left)
            self.count -= 1
            if self.count == 0:
                self.val = node.val
                return
            if node.right: helper(node.right)

        helper(root)
        return self.val
