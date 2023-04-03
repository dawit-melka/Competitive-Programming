class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ ((1 << math.floor(math.log(num, 2) + 1)) -1)
