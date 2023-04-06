n = int(input())
count = 0
for _ in range(n):
    curr = list(map(int, input().split()))
    for j in curr:
        count += j

print(count // 2)
