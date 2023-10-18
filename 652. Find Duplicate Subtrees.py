# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTrees = defaultdict(int)
        result = []
        def dfs(node):
            if not node:
                return "null"
            currVal = str(node.val)
            leftSubtree = dfs(node.left)
            rightSubtree = dfs(node.right)
            serialized = ",".join([currVal, leftSubtree, rightSubtree])
            if subTrees[serialized] == 1:
                result.append(node)
            subTrees[serialized] += 1
            return serialized
        dfs(root)
        return result
        
