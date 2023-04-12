class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPermut = []
        self.usedIndexs = 0
        
        def backtrack(pro):
            if len(pro) == len(nums):
                allPermut.append(pro.copy())
                return

            for i in range(len(nums)):
                if self.usedIndexs & (1 << i):
                    continue 

                self.usedIndexs = self.usedIndexs | (1 << i)
                pro.append(nums[i])
                backtrack(pro)
                pro.pop()
                self.usedIndexs = self.usedIndexs ^ (1 << i)
        
        backtrack([])
        return allPermut
