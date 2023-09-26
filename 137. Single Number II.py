class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        loanly_num = 0
        for i in range(32):
            bitSum = 0
            for num in nums:
                bitSum += (num>>i) & 1

            loanly_num |= (bitSum%3) << i
        
        # convert the result back to two's complement representation if it's negative
        if loanly_num >= 2**31:
            loanly_num -= 2**32
        
        return loanly_num
