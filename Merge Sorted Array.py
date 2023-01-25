class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = m-1
        index2 = n-1
        
        for i in range(n+m-1, -1, -1):
            if index2 < 0:
                break
            if index1 < 0 or nums2[index2] >= nums1[index1]:
                nums1[i] = nums2[index2]
                index2 -= 1
            else:
                nums1[i] = nums1[index1]
                index1 -= 1 
