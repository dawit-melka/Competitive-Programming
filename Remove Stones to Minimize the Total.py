class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        heapify(piles)

        for _ in range(k):
            curr = heappop(piles)
            if curr == 0:
                break
            remove = abs(curr) // 2
            heappush(piles, -(abs(curr) - remove))
        
        return -sum(piles)
