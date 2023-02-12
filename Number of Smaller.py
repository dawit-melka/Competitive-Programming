n, m = map(int, input().strip().split())
arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))
idx1 = 0
result = []
for idx2 in range(len(arr2)):
    while idx1 < len(arr1) and arr1[idx1] < arr2[idx2]:
        idx1 += 1
    result.append(idx1)

print(*result)
