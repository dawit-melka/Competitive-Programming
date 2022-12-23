class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        shortest = math.inf
        idx = -1

        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]

            if x1 == x or y1 == y:
                curr_distance = abs(x - x1) + abs(y - y1)
                if curr_distance < shortest:
                    shortest = curr_distance
                    idx = i
        
        return idx