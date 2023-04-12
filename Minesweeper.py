class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        def inBound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            if not inBound(row, col) or board[row][col] != 'E':
                return 

            count_mines = 0
            board[row][col] = "B"

            for dx, dy in directions:
                if inBound(row+dx, col+dy):
                    if board[row+dx][col+dy] == "M":
                        count_mines += 1
                    

            if count_mines > 0:
                board[row][col] = str(count_mines)
            else:
                for dx, dy in directions:
                    dfs(row+dx, col+dy)

        dfs(r, c)

        return board
            

