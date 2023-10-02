class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ans = 0
        queue = deque([board])
        sortedBoard = [[1,2,3],[4,5,0]]
        visited = set([(tuple(board[0]),tuple(board[1]))])

        while queue:
            for _ in range(len(queue)):
                currBoard = queue.popleft()
                isFound = True
                r0, c0 = 0, 0

                for r in range(2):
                    for c in range(3):
                        if currBoard[r][c] != sortedBoard[r][c]:
                            isFound = False
                            break
                    if not isFound:
                        break

                if isFound: 
                    return ans
                
                for r in range(2):
                    for c in range(3):
                        if currBoard[r][c] == 0:
                            r0, c0 = r, c
                            break
                print(r0, c0)
                
                # swap with top
                if r0 == 1:
                    nextBoard = [row.copy() for row in currBoard]
                    
                    nextBoard[r0][c0], nextBoard[0][c0] = nextBoard[0][c0], nextBoard[r0][c0]
                    tupleNextBoard = (tuple(nextBoard[0]), tuple(nextBoard[1]))
                    if tupleNextBoard not in visited:
                        visited.add(tupleNextBoard)
                        queue.append(nextBoard)

                # swap with bottom
                else:
                    nextBoard = [row.copy() for row in currBoard]
                    nextBoard[r0][c0], nextBoard[1][c0] = nextBoard[1][c0], nextBoard[r0][c0]
                    tupleNextBoard = (tuple(nextBoard[0]), tuple(nextBoard[1]))
                    if tupleNextBoard not in visited:
                        visited.add(tupleNextBoard)
                        queue.append(nextBoard)

                # swap with left
                if c0 > 0:
                    nextBoard = [row.copy() for row in currBoard]
                    nextBoard[r0][c0], nextBoard[r0][c0-1] = nextBoard[r0][c0-1], nextBoard[r0][c0]
                    tupleNextBoard = (tuple(nextBoard[0]), tuple(nextBoard[1]))
                    
                    if tupleNextBoard not in visited:
                        visited.add(tupleNextBoard)
                        queue.append(nextBoard)

                # swap with right
                if c0 < 2:
                    nextBoard = [row.copy() for row in currBoard]
                    nextBoard[r0][c0], nextBoard[r0][c0+1] =nextBoard[r0][c0+1], nextBoard[r0][c0]
                    tupleNextBoard = (tuple(nextBoard[0]), tuple(nextBoard[1]))
                    if tupleNextBoard not in visited:
                        visited.add(tupleNextBoard)
                        queue.append(nextBoard)
            ans += 1
                
        return -1
        
