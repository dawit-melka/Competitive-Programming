class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_x, count_o = 0, 0
        win = ["XXX", "OOO"]
        self.winner = None

        # function to check if both x and o winnes in a game
        def notValidWinner(string):
            if string in win:
                if self.winner and self.winner != string:
                    return True
                else:
                    self.winner = string
            return False

        for row in board:
            #  Check validity of row win
            if notValidWinner(row):
                return False
            
            for char in row:
                if char == "X":
                    count_x += 1
                elif char == "O":
                    count_o += 1

        # valid number of moves is if X advance by one or equal to O
        moves_gap = count_x - count_o
        if moves_gap not in [0, 1]:
            return False

        # Check validity of column win
        col1 = board[0][0]+board[1][0]+board[2][0]
        col2 = board[0][1]+board[1][1]+board[2][1]
        col3 = board[0][2]+board[1][2]+board[2][2]

        if notValidWinner(col1):
            return False
        if notValidWinner(col2):
            return False
        if notValidWinner(col3):
            return False

        # check validity of diagonal win
        diagonal_1 = board[0][0]+board[1][1]+board[2][2]
        diagonal_2 = board[2][0]+board[1][1]+board[0][2]

        if notValidWinner(diagonal_1):
            return False
        if notValidWinner(diagonal_2):
            return False
        
        # if the winner is X the number of moves of X has to exceed by 1
        if self.winner=="XXX" and moves_gap == 0:
            return False
        
        # if the winner is O the number of moves of X and O has to be equal
        if self.winner=="OOO" and moves_gap == 1:
            return False
        
        return True
