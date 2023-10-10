class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        runningSum = 0
        startIndex = -1
        for i in range(len(gas)):
            runningSum += (gas[i] - cost[i])
            if runningSum < 0:
                runningSum = 0
                startIndex = -1
            elif startIndex == -1:
                startIndex = i
        
        return startIndex
