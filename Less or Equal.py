def solution():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
 
    nums.sort()
    if k == 0:
        if nums[0] <= 1:
            return -1
        return nums[0]-1
    if k < n and nums[k] == nums[k-1]:
        return -1
    return nums[k-1]
 
print(solution())
