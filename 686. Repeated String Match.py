class Solution:
    # KMP
    def isSubstring(self, haystack: str, needle: str) -> bool:
        if len(needle) > len(haystack):
            return False
        
        LPS = [0] * len(needle)
        prev = 0
        for i in range(1, len(needle)):
            while prev != 0 and needle[prev] != needle[i]:
                    prev = LPS[prev-1]
            if needle[prev] == needle[i]:
                LPS[i] = prev + 1
                prev += 1
                    
        n = 0
        for h in range(len(haystack)):
            while n != 0 and needle[n] != haystack[h]:
                    n = LPS[n - 1]
            if needle[n] == haystack[h]:
                n += 1
            
            if n == len(needle):
                return True

        return False

    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeatition_needed = ceil(len(b) / len(a))
        curr_a = a * min_repeatition_needed
        if self.isSubstring(curr_a, b):
            return min_repeatition_needed
        if self.isSubstring(curr_a + a, b):
            return min_repeatition_needed + 1

        return -1
        
