class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()
        l, maxFruits = 0, 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            maxFruits = max(maxFruits, r - l + 1)

        return maxFruits
