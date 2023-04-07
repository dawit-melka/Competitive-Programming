class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0

            child_depth = 0
            for child in node.children:
                child_depth = max(child_depth, dfs(child))

            return child_depth + 1

        return dfs(root)
