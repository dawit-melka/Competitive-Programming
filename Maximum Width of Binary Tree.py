class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        max_width = 0

        while q:
            size = len(q)
            _, left = q[0]
            _, right = q[-1]
            max_width = max(max_width, right - left + 1)
            while size:
                size -= 1
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx*2))
                if node.right:
                    q.append((node.right, idx*2 + 1))
        
        return max_width
