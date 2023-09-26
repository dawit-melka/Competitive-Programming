class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def dfs(clipboard, aString):
            if aString == n:
                return 0
            if clipboard > n or aString > n:
                return float("inf")
            if (clipboard, aString) not in memo:
                copy = float("inf")
                if aString > clipboard:
                    copy = dfs(aString, aString)
                paste = float("inf")
                if clipboard > 0:
                    paste = dfs(clipboard, aString + clipboard)
                
                memo[(clipboard, aString)] = 1 + min(copy, paste)
            return memo[(clipboard, aString)]
        
        return dfs(0, 1)
