class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left_ones = 0
        right_ones = 0
        left_operations = 0
        right_operations = 0
        min_operations = []

        for i, num in enumerate(boxes):
            right_ones += int(num)
            right_operations += i* int(num)

        for i in range(len(boxes)):
            min_operations.append(right_operations + left_operations)
            right_ones -= int(boxes[i])
            right_operations -= right_ones 
            left_ones += int(boxes[i])
            left_operations += left_ones

        return min_operations
