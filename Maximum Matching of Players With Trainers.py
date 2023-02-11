class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matches = 0
        j = len(trainers)-1

        for i in range(len(players)-1, -1, -1):
            if players[i] <= trainers[j]:
                matches += 1
                j -= 1
                if j < 0: break
        
        return matches
