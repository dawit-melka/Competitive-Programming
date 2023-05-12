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
        
                
        
        
        
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends