class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        fair_sum = skill[0] + skill[-1]
        left, right = 0, len(skill)-1
        chemistry_sum = 0
        
        while left < right:
            curr_skill = skill[left] + skill[right]
            if curr_skill != fair_sum:
                return -1
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry_sum
