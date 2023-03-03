class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        smallest_count = []

        def countSmallest(word):
            curr = word[0]
            count = 0
            for char in word:
                if char < curr:
                    curr = char
                    count = 0
                if char == curr:
                    count += 1
            return count

        for word in words:
            curr = countSmallest(word)
            smallest_count.append(curr)

        smallest_count.sort()
        res = []
        for word in queries:
            curr = countSmallest(word)
            low, high = -1, len(words)
            while high > low + 1:
                mid = (high + low) // 2

                if smallest_count[mid] <= curr:
                    low = mid
                else:
                    high = mid

            res.append(len(words) - high)

        return res
