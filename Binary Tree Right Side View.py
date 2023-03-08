class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []

        while q:
            size = len(q)
            notInserted = True
            while size:
                node = q.popleft()
                size -= 1
                if notInserted:
                    res.append(node.val)
                    notInserted = False

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return res
