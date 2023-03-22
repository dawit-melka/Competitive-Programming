t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    left, right = -1, (a + b) // 4 + 1

    while right > left + 1:
        mid = (right + left) // 2
        if mid <= min(a, b):
            left = mid
        else:
            right = mid
    
    print(left)
