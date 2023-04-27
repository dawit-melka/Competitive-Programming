class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([root])
        result = []

        while que:
            l = len(que)
            total = 0

            for _ in range(l):
                node = que.popleft()
                total += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
            result.append(total/l)
        
        return result
