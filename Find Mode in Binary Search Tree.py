class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.freq = Counter()
        def traverse(node):
            if not node:
                return
            self.freq[node.val] += 1
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        maxCount = max(self.freq.values())
        mode = []

        for val in self.freq:
            if self.freq[val] == maxCount:
                mode.append(val)
                
        return mode
