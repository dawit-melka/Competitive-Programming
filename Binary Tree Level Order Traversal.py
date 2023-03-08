class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        levelOrder = []
        if root:
            q.append(root)
        while q:
            size = len(q)
            curr = []
            while size:
                size -= 1
                node = q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelOrder.append(curr)

        return levelOrder
