class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        collected = {}
        self.traverse(root, collected, 0, 0)
        cols = [t[1] for t in sorted(collected.items(), key = lambda x: x[0])]
        res = []

        for currCol in cols:
            curr = [t[1] for t in sorted(currCol.items(), key = lambda x: x[0])]
            collectCol = []
            for arr in curr:
                collectCol += sorted(arr)
                
            res.append(collectCol)
        return res

    def traverse(self, node, collected, row, col):
        if not node: return 
        collected[col] = collected.get(col, {})
        collected[col][row] = collected[col].get(row, [])
        collected[col][row].append(node.val)

        self.traverse(node.left, collected, row + 1, col - 1)
        self.traverse(node.right, collected, row + 1, col + 1)
    
