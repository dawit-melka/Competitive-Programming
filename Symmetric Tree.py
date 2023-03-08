class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def notPlindrome(arr):
            left, right = 0, len(arr)-1
            while right > left:
                if arr[left] != arr[right]:
                    return True
                left += 1
                right -= 1
            return False
        
        q = deque()
        q.append(root)
        while q:
            currLevel = []
            size = len(q)
            while size:
                size -= 1
                node = q.popleft()
                if node.left:
                    currLevel.append(node.left.val)
                    q.append(node.left)
                else:
                    currLevel.append(None)
                    
                if node.right:
                    currLevel.append(node.right.val)
                    q.append(node.right)
                else:
                    currLevel.append(None)
            
            if notPlindrome(currLevel):
                return False
        
        return True
