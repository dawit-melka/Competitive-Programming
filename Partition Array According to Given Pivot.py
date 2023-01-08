class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        for n in nums:
            if n < pivot:
                result.append(n)

        for n in nums:
            if n == pivot:
                result.append(n)
        
        for n in nums:
            if  n > pivot:
                result.append(n)

        return result
