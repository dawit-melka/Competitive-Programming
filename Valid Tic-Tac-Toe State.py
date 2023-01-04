class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_X = 0
        count_O = 0
        winner = None

        for row in board:
            if row == "XXX" or row == "OOO":
                if not winner:
                    winner = row
                elif winner != row:
                    return False
            for char in row:
                if char == "X":
                    count_X += 1
                elif char == "O":
                    count_O += 1
        
        diff = count_X - count_O
        if diff != 0 and diff !=1:
            return False
        
        for col in range(3):
            curr_col = ""
            for row in range(3):
                curr_col += board[row][col]
            if curr_col == "XXX" or curr_col == "OOO":
                if not winner:
                    winner = curr_col
                else:
                    if winner != curr_col:
                        return False

        diagonal_1 = board[2][0]+board[1][1]+board[0][2]
        diagonal_2 = board[0][0]+board[1][1]+board[2][2]
        if diagonal_1 == "XXX" or diagonal_1=="OOO":
            if winner:
                if winner != diagonal_1:
                    return False
            else:
                winner = diagonal_1
        
        if diagonal_2 == "XXX" or diagonal_2=="OOO":
            if winner:
                if winner != diagonal_2:
                    return False
            else:
                winner = diagonal_2

        if winner == "XXX" and diff == 0:
            return False
        if winner == "OOO" and diff == 1:
            return False
        return True
        
        
