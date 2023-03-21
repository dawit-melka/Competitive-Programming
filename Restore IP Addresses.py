class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4: return []
        result = []
        curr = []
        def backtrack(idx):
            if idx >= len(s):
                if len(curr) == 4:
                    result.append(".".join(curr))
                return 
            if len(curr) >= 4:
                return
            
            for i in range(idx, min(idx+3, len(s))):
                
                currVal = s[idx: i+1]
                if int(currVal) > 255: return
                curr.append(currVal)
                backtrack(i+1)
                curr.pop()
                if s[idx] == "0": return

        backtrack(0)
        return result
