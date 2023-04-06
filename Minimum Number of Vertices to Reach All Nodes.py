class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        result = []

        for src, dst in edges:
            indegree[dst] += 1


        for i in range(n):
            if not indegree[i]:
                result.append(i)

        return result
