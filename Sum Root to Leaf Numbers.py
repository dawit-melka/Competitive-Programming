class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def backtrack(node, cumm_sum):
            if not node: 
                return 0

            cumm_sum = cumm_sum * 10 + node.val
            if not node.left and not node.right:
                return cumm_sum

            return backtrack(node.left, cumm_sum) + backtrack(node.right, cumm_sum)

        return backtrack(root, 0)
