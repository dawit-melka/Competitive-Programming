t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    find_negative = True
    if nums[0] < 0:
        find_negative = False
    result = 0
    cur_max = nums[0]
    for num in nums:
        if (find_negative and num > 0) or (not find_negative and num < 0):
            cur_max = max(cur_max, num)
        else:
            result += cur_max
            cur_max = num
            find_negative = not find_negative
    
    result += cur_max
    
    print(result)
