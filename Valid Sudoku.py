class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_values = defaultdict(set)
        col_values = defaultdict(set)
        cell_values= defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                curr_val = board[r][c]
                if r in row_values:
                    if curr_val in row_values[r]:
                        return False
                row_values[r].add(curr_val)

                if c in col_values:
                    if curr_val in col_values[c]:
                        return False
                col_values[c].add(curr_val)

                curr_cell = (r//3, c//3)
                if curr_cell in cell_values:
                    if curr_val in cell_values[curr_cell]:
                        return False
                cell_values[curr_cell].add(curr_val)

        return True
