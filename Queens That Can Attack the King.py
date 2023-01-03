class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens_set = set()
        for position in queens:
            queens_set.add(tuple(position))

        
        def search_up(r, c):
            while r-1 >= 0:
                r -= 1
                if (r, c) in queens_set:
                    return [r, c]
            
            return False

        def search_down(r, c):
            while r+1 < 8:
                r += 1
                if (r, c) in queens_set:
                    return [r, c]
            
            return False

        def search_right(r, c):
            while c+1 < 8:
                c += 1
                if (r, c) in queens_set:
                    return [r, c]
            
            return False

        def search_left(r, c):
            while c-1 >= 0:
                c -= 1
                if (r, c) in queens_set:
                    return [r, c]
            
            return False

        def search_up_right(r, c):
            while c+1 < 8 and r-1 >= 0:
                c += 1
                r -= 1
                if (r, c) in queens_set:
                    return [r, c]
            
            return False

        def search_up_left(r, c):
            while c-1 >= 0 and r-1 >= 0:
                c -= 1
                r -= 1
                if (r, c) in queens_set:
                    return [r, c]
            
            return False

        def search_down_right(r, c):
            while c+1 < 8 and r+1 < 8:
                c += 1
                r += 1
                if (r, c) in queens_set:
                    return [r, c]
            
            return False

        def search_down_left(r, c):
            while c-1 >= 0 and r+1 < 8:
                c -= 1
                r += 1
                if (r, c) in queens_set:
                    return [r, c]
            
            return False

        xKing, yKing = king
        
        up_queen = search_up(xKing, yKing)
        down_queen = search_down(xKing, yKing)
        right_queen = search_right(xKing, yKing)
        left_queen = search_left(xKing, yKing)
        up_right_queen = search_up_right(xKing, yKing)
        up_left_queen = search_up_left(xKing, yKing)
        down_right_queen = search_down_right(xKing, yKing)
        down_left_queen = search_down_left(xKing, yKing)

        attacker_queens = []

        if up_queen:
            attacker_queens.append(up_queen)
        if down_queen:
            attacker_queens.append(down_queen)
        if right_queen:
            attacker_queens.append(right_queen)
        if left_queen:
            attacker_queens.append(left_queen)
        if up_right_queen:
            attacker_queens.append(up_right_queen)
        if up_left_queen:
            attacker_queens.append(up_left_queen)
        if down_right_queen:
            attacker_queens.append(down_right_queen)
        if down_left_queen:
            attacker_queens.append(down_left_queen)

        return attacker_queens
