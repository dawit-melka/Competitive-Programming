class Solution:
    def calcGCD(self, num1, num2):
        if not num2:
            return num1

        return self.calcGCD(num2, num1 % num2)


    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            cur_gcd = nums[i]
            for j in range(i+1, len(nums)):
                cur_gcd = self.calcGCD(nums[j], cur_gcd)

                if cur_gcd == k:
                    count += 1
                elif cur_gcd < k:
                    break
            
            if nums[i] == k:
                count += 1

        return count
        
