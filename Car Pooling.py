class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        distance = [0]*1002

        for num, start, end in trips:
            distance[start] += num
            distance[end] -= num

        for i  in range(1001):
            distance[i] += distance[i-1]
            
        for i in range(1001):
            if distance[i] > capacity:
                return False

        return True
