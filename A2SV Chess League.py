n, k = map(int, input().split())
rank = list(map(int, input().split()))
indexs = [i for i in range(1, len(rank)+1)]

def mergeSort(left, right):
    if left > right:
        return []
    if left == right:
        return [indexs[left]]
    
    mid = (left + right) // 2
    leftSorted = mergeSort(left, mid)
    rightSorted = mergeSort(mid+1, right)

    return merge(leftSorted, rightSorted)

def merge(leftArr, rightArr):
    index1, index2 = 0, 0
    merged = []

    while index1 < len(leftArr) and index2 < len(rightArr):
        num1, num2 = rank[leftArr[index1]-1], rank[rightArr[index2]-1]
        if num1 < num2:
            if num2 - num1 <= k:
                merged.append(leftArr[index1])
            index1 += 1
        else:
            if num1 - num2 <= k:
                merged.append(rightArr[index2])
            index2 += 1

    merged.extend(leftArr[index1:])
    merged.extend(rightArr[index2:])

    return merged

result = sorted(mergeSort(0, len(rank) - 1))

print(*result)
