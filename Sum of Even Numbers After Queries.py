class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if num%2 == 0:
                even_sum += num
        
        answer = []

        for val, i in queries:
            new_val = nums[i] + val

            if nums[i]%2:
                if new_val%2 == 0:
                    even_sum += new_val
            else:
                if new_val%2 == 0:
                    even_sum += val
                else:
                    even_sum -= nums[i]

            answer.append(even_sum)
            nums[i] = new_val

        return answer
