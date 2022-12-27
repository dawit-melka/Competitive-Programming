from collections import defaultdict

n_m = list(map(int, input().split()))
n = n_m[0]
m = n_m[1]
indexs = defaultdict(list)

for i in range(n):
    char = input()
    indexs[char].append(i+1)
    
for i in range(m):
    char  = input()
    if len(indexs[char]):
        string =" ".join(map(str, indexs[char]))
    else:
        string = "-1"
    print(string)
