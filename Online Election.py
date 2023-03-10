class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        currMax = persons[0]
        freq = Counter()
        for i in range(len(persons)):
            freq[persons[i]] += 1
            if freq[persons[i]] >= freq[currMax]:
                currMax = persons[i]
            persons[i] = currMax    

    def q(self, t: int) -> int:
        left = -1
        right = len(self.times)
        while right > left + 1:
            mid = (left + right) // 2
            if self.times[mid] > t:
                right = mid
            else:
                left = mid
        
        return self.persons[left]
