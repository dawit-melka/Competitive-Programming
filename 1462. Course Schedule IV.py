class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        prerequisitList = {}
        
        for s, e in prerequisites:
            graph[s].append(e)
        
        def dfs(node):
            if node in prerequisitList:
                return prerequisitList[node]
            childs = set()
            for child in graph[node]:
                curr = dfs(child)
    
                childs.update(curr)
            new =  childs.copy()
            new.add(node)      
            prerequisitList[node] = new
            return new
        
        for i in range(numCourses):
            if i not in prerequisitList:
                dfs(i)
        
        result = []
        for s, e in queries:
            ans = s in prerequisitList and e in prerequisitList[s]
            result.append(ans)
        
        return result
