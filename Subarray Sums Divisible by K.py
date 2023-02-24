class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modulos = {0 : 1}
        running_sum = 0
        count = 0
        
        for num in nums:
            running_sum += num
            curr_mod = running_sum%k
            if curr_mod in modulos:
                count += modulos[curr_mod]
                modulos[curr_mod] += 1
            else:
                modulos[curr_mod] = 1
        
        return count
