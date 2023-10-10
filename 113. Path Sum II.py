# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.allPath = []

        def dfs(node, currPath):
            if not node:
                return
            if not node.left and not node.right:
                
                currPath = currPath + [node.val]
                if sum(currPath) == targetSum:
                    self.allPath.append(currPath)
                return
            dfs(node.left, currPath + [node.val])
            dfs(node.right, currPath + [node.val])

        dfs(root, [])
        return self.allPath
