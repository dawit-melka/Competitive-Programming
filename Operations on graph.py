from collections import defaultdict
n = int(input())
k = int(input())
adj_list = defaultdict(list)

for _ in range(k):
    curr = list(map(int, input().split()))
    if len(curr) == 3:  
        adj_list[curr[1]].append(curr[2])
        adj_list[curr[2]].append(curr[1])
    else:
        print(*adj_list[curr[1]])
