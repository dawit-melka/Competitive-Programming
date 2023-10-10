# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        queue = deque([(root, 1)])
        
        while queue:
            leftIndex = queue[0][1]
            rightIndex = queue[-1][1]
            maxWidth = max(maxWidth, rightIndex - leftIndex + 1)
            for _ in range(len(queue)):
                node, i = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*i))
                if node.right:
                    queue.append((node.right, 2*i + 1))
        
        return maxWidth
        
