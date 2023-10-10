# Brutforce
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            found = True
            for j in range(len(needle)):
                if haystack[i+j] !=needle[j]:
                    found =False
                    break

            if found:
                return i
        return  -1

# Rabin Karp
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        n = len(haystack)
        m = len(needle)
        b = 27 
        hashNeedle = 0
        currHash = 0

        for j in range(m):
            charValNeedle = ord(needle[j]) - ord("a") + 1
            hashNeedle += charValNeedle * (b**(m-j-1))
            
            charValHay = ord(haystack[j]) - ord("a") + 1
            currHash += charValHay * (b**(m-j-1))

        if hashNeedle == currHash:
            return 0
        
        for i in range(len(haystack)-len(needle)):           
            toBePopped = ord(haystack[i]) - ord("a") + 1
            toBeAdded = ord(haystack[i+m]) - ord("a") +1
            currHash -=   (toBePopped * (b**(m-1)))
            currHash = (currHash * b) + toBeAdded
            if currHash == hashNeedle:
                return i+1
          
        
        return  -1


# KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
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
                return h - n + 1

        return -1
        
