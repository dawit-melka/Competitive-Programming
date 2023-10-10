class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_chars_frequency = Counter(s1)
        left = 0
        running_frequency = defaultdict(int)
        for right in range(len(s2)):
            curr_char = s2[right]
            running_frequency[curr_char] += 1
            if curr_char not in s1_chars_frequency:
                while left != right+1:
                    running_frequency[s2[left]] -= 1
                    left += 1
            else:
                while running_frequency[curr_char] > s1_chars_frequency[curr_char]:
                    running_frequency[s2[left]] -= 1
                    left += 1
                if right - left + 1 == len(s1):
                    return True


        return False
