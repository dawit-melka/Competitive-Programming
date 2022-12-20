T = int(input())
for count in range(T):
    n = int(input())
    arr = list(map(int,input().strip().split(' ')))
    
    left = 0
    right = n - 1
    
    res = "Yes"
    cur = max(arr[0], arr[n-1])
    while left < right:
        maximum = max(arr[left], arr[right])
        if maximum > cur:
            res = "No"
            break
        cur = maximum
        if arr[left] > arr[right]:
            left += 1
        else:
            right -= 1
    
    print(res)
