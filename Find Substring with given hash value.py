class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powerK_1 = (power ** (k-1)) % modulo      
        index = 0
        end = len(s) - 1
        hash = 0
        for i in range(len(s)-1, -1, -1):
            sVal = ord(s[i]) - ord('a') + 1
            hash = (hash * power % modulo + sVal) % modulo
            if end - i + 1 == k:
                if hash == hashValue:
                    index = i
                hash = (hash - (ord(s[end]) - ord('a') + 1) * powerK_1) % modulo
                end -= 1

        return s[index: index+k]
