class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_x, count_o = 0, 0
        win = ["XXX", "OOO"]
        self.winner = None

        def notValidWinner(string):
            if string in win:
                if self.winner and self.winner != string:
                    return True
                else:
                    self.winner = string
            return False

        for row in board:
            if notValidWinner(row):
                return False
            
            for char in row:
                if char == "X":
                    count_x += 1
                elif char == "O":
                    count_o += 1
        
        difference = count_x - count_o
        if difference not in [0, 1]:
            return False

        col1 = board[0][0]+board[1][0]+board[2][0]
        col2 = board[0][1]+board[1][1]+board[2][1]
        col3 = board[0][2]+board[1][2]+board[2][2]

        if notValidWinner(col1):
            return False
        if notValidWinner(col2):
            return False
        if notValidWinner(col3):
            return False

        diagonal_1 = board[0][0]+board[1][1]+board[2][2]
        diagonal_2 = board[2][0]+board[1][1]+board[0][2]

        if notValidWinner(diagonal_1):
            return False
        if notValidWinner(diagonal_2):
            return False
        
        if self.winner=="XXX" and difference == 0:
            return False
        if self.winner=="OOO" and difference == 1:
            return False
        
        return True
