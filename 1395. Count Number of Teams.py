class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count_greater_lower = []
        team_count = 0
        for i in range(len(rating)):
            count_greater = 0
            count_lower = 0
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    count_greater += 1
                else:
                    count_lower += 1
            count_greater_lower.append((count_greater, count_lower))
        
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    team_count += count_greater_lower[j][0]
                else:
                    team_count += count_greater_lower[j][1]

        return team_count
        
