# Approach 1:
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


# Approach 2: Backtracking
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
