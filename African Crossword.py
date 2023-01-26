n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
count_row_chars = {}
count_col_chars = {}
for r in range(n):
    count_row_chars[r] = [0]*26
    for c in range(m):
        if c not in count_col_chars:
            count_col_chars[c] = [0]*26
        count_row_chars[r][ord(grid[r][c]) - ord("a")] += 1
        count_col_chars[c][ord(grid[r][c]) - ord("a")] += 1

result = []

for r in range(n):
    for c in range(m):
        if count_row_chars[r][ord(grid[r][c]) - ord("a")] <= 1 and count_col_chars[c][ord(grid[r][c]) - ord("a")] <= 1:
            result.append(grid[r][c])

result = "".join(result)
print(result)
