class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum = [0]*(n)

        for shift in shifts:
            start, end, direction = shift
            if not direction:
                direction = -1
            prefix_sum[start] += direction
            if end + 1 < n:
                prefix_sum[end + 1] += -direction
        
        # build prefix sum
        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]

        result = []

        for i in range(n):
            shift = ord(s[i]) - ord("a") + prefix_sum[i] 
            shift %= 26
            curr = chr(97 + shift)
            result.append(curr)

        return "".join(result)
