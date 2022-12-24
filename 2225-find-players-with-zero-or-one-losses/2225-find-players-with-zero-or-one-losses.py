class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        one_losers = set()
        all_winners = set()
        losers = set()

        for winner, loser in matches:
            if winner not in losers:
                all_winners.add(winner)
            if loser in all_winners:
                all_winners.remove(loser)
                
            if loser in one_losers:
                one_losers.remove(loser)
            if loser not in losers:
                one_losers.add(loser)
                
            losers.add(loser)

        return [sorted(all_winners), sorted(one_losers)]
