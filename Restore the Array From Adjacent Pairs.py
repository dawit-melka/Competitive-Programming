class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        start = -1
        adj_list = defaultdict(list)
        for node1, node2 in adjacentPairs:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
        
        for node in adj_list:
            if len(adj_list[node]) == 1:
                start = node
                break
        stack = deque([start])
        result = []
        visited = set([start])
        
        while stack:
            curr = stack.pop()
            result.append(curr)

            for ngh in adj_list[curr]:
                if ngh not in visited:
                    visited.add(ngh)
                    stack.append(ngh)
        
        return result
