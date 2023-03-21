class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = 0
        curr = []

        def backtrack(idx):
            nonlocal result
            result = max(result, len("".join(curr)))

            if idx >= len(arr): return

            curr.append(arr[idx])
            temp = "".join(curr)
            if len(temp) == len(set(list(temp))):
                backtrack(idx + 1)
            curr.pop()
            backtrack(idx + 1)

        backtrack(0)

        return result
