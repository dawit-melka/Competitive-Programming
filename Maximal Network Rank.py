class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        result = 0

        for src, dst in roads:
            adj_list[src].add(dst)
            adj_list[dst].add(src)
            
        for node1 in adj_list:
            for node2 in adj_list:
                if node1 == node2:
                    continue
                curr = len(adj_list[node1]) + len(adj_list[node2])
                if node1 in adj_list[node2]:
                    result = max(result, curr-1)
                else:
                    result = max(result, curr)
        

        return result
