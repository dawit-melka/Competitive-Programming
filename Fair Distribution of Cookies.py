class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = float("inf")
        cookies.sort(reverse = True)
        childCookies = [0]*k

        def backtrack(idx, curr, cookies):
            nonlocal res
            if max(curr) >= res:
                return
            if idx == len(cookies):
                res = min(res, max(curr))
                return

            
            for j in range(k):
                curr[j] += cookies[idx]
                backtrack(idx + 1, curr, cookies)
                curr[j] -= cookies[idx]

        backtrack(0, childCookies, cookies)
        return res
