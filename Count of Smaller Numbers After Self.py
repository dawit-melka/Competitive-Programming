class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            nums[i] = (nums[i], i)

        def mergeSort(left, right):
            if left > right: 
                return []
            if left == right: 
                return [nums[left]]
            
            mid = (left + right) // 2
            leftSorted = mergeSort(left, mid)
            rightSorted = mergeSort(mid + 1, right)

            return merge(leftSorted, rightSorted)

        def merge(left, right):

            index2 = len(right) - 1

            for index1  in range(len(left)-1, -1, -1):
                val, i = left[index1]
                while index2 >= 0 and val <= right[index2][0]:
                    index2 -= 1
                if index2 < 0: 
                    break

                result[i] += index2 + 1 

            index1, index2 = 0, 0
            merged = []
            while index1 < len(left) and index2 < len(right):
                if left[index1][0] < right[index2][0]:
                    merged.append(left[index1])
                    index1 += 1
                else:
                    merged.append(right[index2])
                    index2 += 1

            merged.extend(left[index1:])
            merged.extend(right[index2:])

            return merged


        mergeSort(0, len(nums)-1)

        return result



