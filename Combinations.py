class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.allCombinations = []

        def backtrack(n, i, k, combination):
            if len(combination) == k:
                self.allCombinations.append(combination.copy())
                return
            if i > n: return  
            
            combination.append(i)
            backtrack(n, i+1, k, combination)
            combination.pop()
            backtrack(n, i+1, k, combination)

        backtrack(n, 1, k, [])

        return self.allCombinations
            
