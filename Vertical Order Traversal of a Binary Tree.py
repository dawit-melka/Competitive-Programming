class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        collected = defaultdict(list)
        self.traverse(root, collected, 0, 0)
        collected = list(dict(sorted(collected.items())).values())
        
        for i in range(len(collected)):
            collected[i] = [val for (j, val) in sorted(collected[i])]

        return collected

    def traverse(self, node, collected, row, col):
        if not node: return

        collected[col].append((row, node.val))
        self.traverse(node.left, collected, row + 1, col - 1)
        self.traverse(node.right, collected, row + 1, col + 1)
