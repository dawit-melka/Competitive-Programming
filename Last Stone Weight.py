class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones)

        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            diff = abs(x - y)
            if diff > 0:
                heappush(stones, -diff)
        
        if not stones:
            return 0
        return abs(heappop(stones))
