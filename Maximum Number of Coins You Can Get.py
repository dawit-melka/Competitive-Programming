class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        max_coins = 0
        n = 2*(len(piles)//3)
        for i in range(1, n, 2):
            max_coins += piles[i]
        
        return max_coins
