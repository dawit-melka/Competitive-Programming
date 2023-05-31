# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        
        graph = defaultdict(set)
        result = []
        queue = deque()
        queue.append(target.val)
        def dfs(node): 
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)
                dfs(node.right)
        dfs(root)
        count = 0
        visited = set([target.val])

        while queue:
            size = len(queue)
            
            for _ in range(size):
                curr = queue.popleft()
                for ngh in graph[curr]:
                    if ngh not in visited:
                        visited.add(ngh)
                        queue.append(ngh)
            count += 1
            
            if count == k:
                return list(queue)
        
        return []
