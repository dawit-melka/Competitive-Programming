class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        
        heap = []
        curr_time = 0
        index = 0
        result = []
        
        while index < len(tasks) or heap:
            if not heap:
                curr_time = tasks[index][0]
            else:
                process_time, idx = heappop(heap)
                curr_time += process_time
                result.append(idx)
                
            while index < len(tasks) and tasks[index][0] <= curr_time:
                heappush(heap, (tasks[index][1], tasks[index][2]))
                index += 1
        
        return result
