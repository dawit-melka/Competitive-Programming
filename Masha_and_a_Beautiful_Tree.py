

def solution():
    def mergeSort(nums):
        nonlocal swaps

        n = len(nums)
        if n == 1:
            return nums
        
        left = mergeSort(nums[:n//2])
        right = mergeSort(nums[n//2:])

        if not left or not right:
            return
        if left[-1] + 1 == right[0]:
            return left + right
        elif right[-1] + 1 == left[0]:
            swaps += 1
            return right + left
        
        return

    t = int(input())
    for _ in range(t):
        m = int(input())
        leafs = list(map(int, input().split()))
        swaps = 0
        if not mergeSort(leafs):
            print(-1)
        else:
            print(swaps)

    
solution()
