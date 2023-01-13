import sys
from collections import Counter
input = sys.stdin.readline
            

def main():
    t = int(input())
    
    for _ in range(t):
        ROWS, COLS = map(int, input().split())
        matrix = []
        for _ in range(ROWS):
            matrix.append(list(map(int, input().split())))
        
        up_diagonals_sum = Counter()
        down_diagonals_sum = Counter()
        
        for r in range(ROWS):
            for c in range(COLS):
                up_diagonals_sum[r+c] += matrix[r][c]
                down_diagonals_sum[r-c] += matrix[r][c]
                
        maxAttack = 0
        for r in range(ROWS):
            for c in range(COLS):
                currAttack = up_diagonals_sum[r+c] + down_diagonals_sum[r-c] - matrix[r][c]
                maxAttack = max(maxAttack, currAttack)
        
        print(maxAttack)
        
if __name__ == "__main__":
    main()
