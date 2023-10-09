class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            v1, v2 = equations[i]
            graph[v1].append((v2, values[i]))
            graph[v2].append((v1, 1/values[i]))
        visited = set()
        def dfs(currVar, target, ans):
            if currVar not in graph:
                return -1
            if currVar == target:
                return ans
            
            visited.add(currVar)
            for child, mult in graph[currVar]:
                if child not in visited:
                    curr_ans = dfs(child, target, ans*mult)
                    if curr_ans > 0:
                        return curr_ans
            
            return -1
        result = []
        for src, dest, in queries:
            visited = set()
            result.append(dfs(src, dest, 1))

        return result
