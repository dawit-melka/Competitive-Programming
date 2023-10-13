class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        def count(i, spots):
            if i <= 0 or spots <= 0:
                return 1
            val = (spots *(spots-1))//2
            return val * count(i-1, spots-2)
        
        return count(n, 2*n) % MOD
        
