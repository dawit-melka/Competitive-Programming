n, m = map(int, input().strip().split())
arr_one = list(map(int, input().strip().split()))
arr_two = list(map(int, input().strip().split()))

index1, index2 = 0, 0
result = []

while index1 < n or index2 < m:
    if index1 < n and index2 < m:
        if arr_one[index1] < arr_two[index2]:
            result.append(arr_one[index1])
            index1 += 1
        else:
            result.append(arr_two[index2])
            index2 += 1
    elif index1 < n:
        result.append(arr_one[index1])
        index1 += 1
    else:
        result.append(arr_two[index2])
        index2 += 1

print(*result)


