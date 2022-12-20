n_m = list(map(int,input().strip().split(' ')))
n = n_m[0]
m = n_m[1]
arr = list(map(int,input().strip().split(' ')))
A = set(map(int,input().strip().split(' ')))
B = set(map(int,input().strip().split(' ')))

happiness = 0

for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)
