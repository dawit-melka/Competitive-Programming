class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]

        self.count = 0
        def mergeSort(left, right):
            if left > right: return []
            if left == right:
                return [nums1[right]]
            mid = (left + right) // 2
            leftSorted = mergeSort(left, mid)
            rightSorted = mergeSort(mid+1, right)
            return merge(leftSorted, rightSorted)

        def merge(leftArr, rightArr):
            merged = []
            index = 0
            for num in leftArr:
                while index < len(rightArr) and num > rightArr[index] + diff:
                    index += 1
                if index == len(rightArr):
                    break
                self.count += len(rightArr) - index
            
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
            
            return merged
        mergeSort(0, len(nums1)-1)
        return self.count
