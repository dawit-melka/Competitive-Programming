import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        prev_square = set()
        for i in range(ceil(math.sqrt(c))+1):
            if (c - i*i) in prev_square or 2*(i*i) == c:
                return True
            prev_square.add(i*i)
        return False
