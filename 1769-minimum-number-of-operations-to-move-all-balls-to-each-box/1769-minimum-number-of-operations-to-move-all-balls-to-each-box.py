class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left_balls = 0
        right_balls = 0
        left_operations = 0
        right_operations = 0
        min_operations = []
        
        # Get the total number of balls and operations required for i = 0
        for i, num in enumerate(boxes):
            right_balls += int(num)
            right_operations += i* int(num)
         
        # starting from right iterate to left
        # decrement right operations and right balls
        # increament left operations and left balls
        for i in range(len(boxes)):
            min_operations.append(right_operations + left_operations)
            right_balls -= int(boxes[i])
            right_operations -= right_balls 
            left_balls += int(boxes[i])
            left_operations += left_balls

        return min_operations
