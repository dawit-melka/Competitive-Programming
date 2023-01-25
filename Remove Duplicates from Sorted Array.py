class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seeker, holder = 1, 1
        
        while seeker < len(nums):
            if nums[seeker] != nums[seeker-1]:
                nums[holder] = nums[seeker]
                holder += 1
            seeker += 1
            
        return holder
