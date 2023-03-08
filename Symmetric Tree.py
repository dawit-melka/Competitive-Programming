class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(Lnode, Rnode):
            if not Lnode and not Rnode:
                return True
            if not Lnode or not Rnode or Lnode.val != Rnode.val:
                return False
            
            return check(Lnode.left, Rnode.right) and check(Lnode.right, Rnode.left)
            
        return check(root.left, root.right)
