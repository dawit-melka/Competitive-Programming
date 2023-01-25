class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        last = 0
        prev_part_end = -1
        last_occurence = {}
        
        for i, char in enumerate(s):
            last_occurence[char] = i

        for i in range(len(s)):
            last_idx = last_occurence[s[i]]
            last = max(last_idx, last)

            if i == last:
                result.append(last - prev_part_end)
                prev_part_end = last

        return result
