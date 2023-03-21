class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count_paths = 0

        def traverse(node, pathSum, runningSum):
            nonlocal count_paths
            if not node: return
            runningSum += node.val
            count_paths += pathSum[runningSum - targetSum]
            
            pathSum[runningSum] += 1
            traverse(node.left, pathSum, runningSum)
            traverse(node.right, pathSum, runningSum)
            pathSum[runningSum] -= 1


        traverse(root, Counter([0]), 0)

        return count_paths
