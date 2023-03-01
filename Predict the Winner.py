class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def findTheWinner(l, r, isPlayer1):
            if r == l:
                if isPlayer1:
                    return (nums[r], 0)
                else:
                    return (0, nums[r])
            p1l, p2l = findTheWinner(l+1, r, not isPlayer1)
            p1r, p2r = findTheWinner(l, r-1, not isPlayer1)
            if isPlayer1:
                if nums[l] + p1l >= nums[r] + p1r:
                    return (p1l + nums[l], p2l)
                return (p1r + nums[r], p2r)
            
            if nums[l] + p2l >= nums[r] + p2r:
                return (p1l, p2l + nums[l])
            return (p1r, p2r + nums[r])

        p1_score, p2_score = findTheWinner(0, len(nums)-1, True)

        return p1_score >= p2_score
