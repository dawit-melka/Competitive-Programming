class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = {}
        res = 0
        MOD = pow(10, 9) + 7

        for rate in deliciousness:
            for i in range(22):
                sqr = pow(2, i)
                target = sqr - rate
                if target in count:
                    res += count[target]
            if rate in count:
                count[rate] += 1
            else:
                count[rate] = 1
        
        return res % MOD
