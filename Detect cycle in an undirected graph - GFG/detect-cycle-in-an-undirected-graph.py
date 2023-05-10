from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        curr_path = set()
        visited = set()
		def dfs(parent, node):
            if node in curr_path:
                return False
            if node in visited:
                return True
            visited.add(node)
            curr_path.add(node)
		    
            for ngh in adj[node]:
                if ngh != parent:
                    if not dfs(node, ngh):
                        return False
		    
            curr_path.remove(node)
            return True
		 
		for i in range(V):
		     if not dfs(-1, i):
		         return True
		  
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends