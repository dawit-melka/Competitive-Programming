class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = defaultdict(list)
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        result = [0] * n
        
        def dfs(node, parent):

            map_ = Counter()
            map_[labels[node]] += 1
            for ngh in adj_list[node]:
                if ngh != parent:
                    map_ += dfs(ngh, node)
            
            result[node] = map_[labels[node]]

            return map_
        
        dfs(0, -1)

        return result
