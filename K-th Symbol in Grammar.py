class Solution:
    
    def findVal(self, left, right, n, k):
        if right == left + 1:
            return n

        mid = (right + left) // 2
        if mid >= k:
            return self.findVal(left, mid, n, k) 
        else:
            return self.findVal(mid, right, (n+1)%2, k)


    def kthGrammar(self, n: int, k: int) -> int:
        return self.findVal(0, 2**(n-1)+1, 0, k)
