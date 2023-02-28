class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = (10**9) + 7
        stack = []
        start = [0]*len(arr)
        res = 0
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                res += arr[idx] * ((idx - start[idx] + 1) * (i - idx))
            if stack:
                start[i] = stack[-1] + 1
            stack.append(i)

        while stack:
            idx = stack.pop()
            res += arr[idx]*((idx - start[idx] + 1) * (len(arr)-idx))

        return res % MOD 
