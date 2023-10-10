# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        prevSum = defaultdict(int)
        prevSum[0] = 1
        result = 0
        
        def dfs(node, currSum):
            nonlocal result
            currSum += node.val
            result += prevSum[currSum - targetSum]
            prevSum[currSum] += 1

            if node.left:
                dfs(node.left, currSum)
            if node.right:
                dfs(node.right, currSum)
            
            prevSum[currSum] -= 1        
            currSum -= node.val

        dfs(root, 0)
        return result
