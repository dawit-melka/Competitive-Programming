class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        allPaths = []
        def backtrack(node, curr):
            if not node:
                processed = "->".join(list(map(str, curr)))
                allPaths.append(processed)
                return

            curr.append(node.val)
            if node.left and node.right:
                backtrack(node.left, curr)
                backtrack(node.right, curr)
            elif node.left:
                backtrack(node.left, curr)
            else:
                backtrack(node.right, curr)
                
            curr.pop()

        backtrack(root, [])
        return allPaths
