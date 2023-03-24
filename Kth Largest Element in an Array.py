class Solution:
    def quickSort(self,nums, k, left, right):
            pivot = random.randint(left, right)
            # swap the pivot element with the left most element
            nums[pivot], nums[left] = nums[left], nums[pivot]
            write = left+1
            for read in range(left+1, right+1):
                if nums[read] <= nums[left]:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1
            
            nums[left], nums[write-1] = nums[write-1], nums[left]

            if len(nums) - (write - 1) == k:
                return nums[write - 1]
            if len(nums) -(write - 1)  < k:  
                return self.quickSort(nums, k, left, write-2)
            else:
                return self.quickSort(nums, k, write, right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums, k, 0, len(nums)-1)
