n = int(input())

for i in range(1, n+1):
    curr = list(map(int, input().split()))
    adj = []
    for j in range(n):
        if curr[j]:
            adj.append(j+1)

    print(len(adj), *adj)
