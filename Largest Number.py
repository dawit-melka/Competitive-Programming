class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def compare(num1, num2):
            choice1 = num1 + num2
            choice2 = num2 + num1
            return int(choice2) - int(choice1)
        
        nums.sort(key = cmp_to_key(compare))
        
        if nums[0] == "0":
            return "0"
        return "".join(nums)
