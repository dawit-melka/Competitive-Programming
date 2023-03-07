class Solution:
    def invert_(self, binary):
        binary = list(binary)
        for i in range(len(binary)):
            if binary[i] == "0":
                binary[i] = "1"
            else:
                binary[i] = "0"

        return binary
    def buildNthBinary(self, n):
        if n == 1:
            return "0"
        
        curr = self.buildNthBinary(n-1)
        return curr +"1" + "".join(reversed(self.invert_(curr)))
    def findKthBit(self, n: int, k: int) -> str:
        return self.buildNthBinary(n)[k-1]
