class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        numMap = defaultdict(int)
        toRight = True
        count = 1
        for r in range(n-1, -1, -1):
            if toRight:
                for c in range(n):
                    numMap[count] = board[r][c]
                    count += 1
            else:
                for c in range(n-1, -1, -1):
                    numMap[count] = board[r][c]
                    count += 1
            toRight = not toRight

        def bfs():
            queue = deque([1])
            visited = set([1])
            ans = 0
            while queue:
                for _ in range(len(queue)):
                    num = queue.popleft()
                    if num == n*n:
                        return ans
                    for nextNum in range(num + 1, min(n*n, num+6)+1):
                        if numMap[nextNum] != -1:
                            nextNum = numMap[nextNum]
                        
                        if nextNum not in visited:
                            visited.add(nextNum)
                            queue.append(nextNum)
                ans += 1
            
            return -1

        return bfs() 
