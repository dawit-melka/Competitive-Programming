from typing import List
from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]):
        # code here
        indegree = [0] * n
        adj_list = defaultdict(list)
        to_do = deque()
        result = [-1] * n
        visited = set()
        
        for src, dst in edges:
            adj_list[src-1].append(dst-1)
            indegree[dst-1] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                to_do.append((i, 1))
        
        while to_do:
            curr, dis = to_do.popleft()
            if result[curr] == -1:
                result[curr] = dis
            
            for child in adj_list[curr]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    to_do.append((child, dis+1))
        
        return " ".join(map(str,result))
