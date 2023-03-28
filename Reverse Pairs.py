class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.result = 0

        def mergeSort(left, right):
            if left > right:
                return []
            if left == right:
                return [nums[right]]

            mid = (left + right) // 2
            leftSorted = mergeSort(left, mid)
            rightSorted = mergeSort(mid + 1, right)

            return merge(leftSorted, rightSorted)

        def merge(leftArr, rightArr):
            merged = []
            index1, index2 = 0, 0

            while index1 < len(leftArr) and index2 < len(rightArr):
                if leftArr[index1] < rightArr[index2]:
                    merged.append(leftArr[index1])
                    index1 += 1
                else:
                    merged.append(rightArr[index2])
                    index2 += 1

            merged.extend(leftArr[index1:])
            merged.extend(rightArr[index2:])

            index2 = len(rightArr)-1
            for index1 in range(len(leftArr)-1, -1, -1):
                while index2 >= 0 and leftArr[index1] <= 2 * rightArr[index2]:
                    index2 -= 1
                
                if index2 < 0:
                    break
                
                self.result += index2 + 1
            
            return merged

        mergeSort(0, len(nums)-1)

        return self.result
