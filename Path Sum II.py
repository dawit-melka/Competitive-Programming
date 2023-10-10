# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        allPath = []
        currPath = []
        
        def dfs(node, currSum):
            currPath.append(node.val)
            currSum += node.val
            
            if not node.left and not node.right and currSum == targetSum:
                allPath.append(currPath.copy())
            if node.left != None:
                dfs(node.left, currSum)

            if node.right != None:
                dfs(node.right, currSum)

            currPath.pop()
            currSum -= node.val

        dfs(root, 0)
        return allPath
