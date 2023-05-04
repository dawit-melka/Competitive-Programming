class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        heap = []
            
        for word in frequency:
            heappush(heap, (-frequency[word], word))
            
        result = []
        for _ in range(k):
            freq, word = heappop(heap)
            result.append(word)

        return result
