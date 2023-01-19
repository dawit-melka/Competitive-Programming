'''
Approach 1
Time Complexity: O(N*N)
Space Complexity: O(N)
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_arr = sorted(nums)
        result = []
        for num in nums:
            result.append(sorted_arr.index(num))
    
        return result
    
'''
Approach 2: Counting Sort
  k = Max_val - Min_val
Time Complexity: O(N + K)   
Space Complexity: O(K)
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_val = max(nums)
        min_val = min(nums)
        count = [0]*(max_val - min_val + 1)
        for num in nums:
            count[num - min_val] += 1
        running_sum = 0
        for i in range(len(count)):
            temp = count[i]
            count[i] = running_sum
            running_sum += temp
        result = []
        for num in nums:
            result.append(count[num-min_val])
        return result
