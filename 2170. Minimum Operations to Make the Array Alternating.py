class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        oddValsCount = defaultdict(int)
        evenValsCount = defaultdict(int)
        oddMax1 = oddMax2 = evenMax1 = evenMax2 = None
        for i in range(len(nums)):
            if i % 2:
                oddValsCount[nums[i]] += 1
                if oddMax1 == None:
                    oddMax1 = nums[i]
                else:
                    if oddValsCount[nums[i]] >= oddValsCount[oddMax1]:
                        if oddMax1 == nums[i]:
                            continue
                        oddMax2 = oddMax1
                        oddMax1 = nums[i]
                    elif oddMax2 == None or oddValsCount[nums[i]] > oddValsCount[oddMax2]:
                        oddMax2 = nums[i]
            else:
                evenValsCount[nums[i]] += 1
                if evenMax1 == None:
                    evenMax1 = nums[i]
                else:
                    if evenValsCount[nums[i]] >= evenValsCount[evenMax1]:
                        if evenMax1 == nums[i]:
                            continue
                        evenMax2 = evenMax1
                        evenMax1 = nums[i]
                    elif evenMax2 == None or evenValsCount[nums[i]] > evenValsCount[evenMax2]:
                        evenMax2 = nums[i]

        if oddMax1 != evenMax1:
            result = n - oddValsCount[oddMax1] - evenValsCount[evenMax1]
            return result
        if oddMax1 == oddMax2 == evenMax1 == evenMax2:
            return n // 2
        sub = 0
        if oddMax1 != oddMax2:
            sub = oddValsCount[oddMax2] + evenValsCount[evenMax1]

        if evenMax1 != evenMax2:
            sub = max(sub, oddValsCount[oddMax1] + evenValsCount[evenMax2]) 
        
        return n - sub
        
