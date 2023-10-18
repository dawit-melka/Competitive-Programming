class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        prefMap = {}
        for  i in range(n):
            prefMap[i] = {}
            for j in range(n-1):
                prefMap[i][preferences[i][j]] = j
        unhappy = set()
        for i in range(len(pairs)):
            a, b = pairs[i]
            for j in range(i+1, len(pairs)):
                c, d = pairs[j]
                a_prefers_c_than_b = prefMap[a][b] > prefMap[a][c]
                c_prefers_a_than_d = prefMap[c][d] > prefMap[c][a]
                if  a_prefers_c_than_b and c_prefers_a_than_d:
                    unhappy.add(a)
                    unhappy.add(c)
                
                a_prefers_d_than_b = prefMap[a][b] > prefMap[a][d]
                d_prefers_a_than_c = prefMap[d][c] > prefMap[d][a]
                if a_prefers_d_than_b and d_prefers_a_than_c:
                    unhappy.add(a)
                    unhappy.add(d)

                b_prefers_c_than_a = prefMap[b][a] > prefMap[b][c]
                c_prefers_b_than_d = prefMap[c][d] > prefMap[c][b]
                if b_prefers_c_than_a and c_prefers_b_than_d:
                    unhappy.add(b)
                    unhappy.add(c)
                
                b_prefers_d_than_a = prefMap[b][a] > prefMap[b][d]
                d_prefers_b_than_c = prefMap[d][c] > prefMap[d][b]
                if b_prefers_d_than_a and d_prefers_b_than_c:
                    unhappy.add(b)
                    unhappy.add(d)
                
        return len(unhappy)

        
