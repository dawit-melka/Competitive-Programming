n = int(input())
nums = list(map(int, input().split()))
hasEven, hasOdd = False, False
for num in nums:
    if num%2:
        hasOdd = True
    else:
        hasEven = True
    if hasEven and hasOdd:
        nums.sort()
        break

print(*nums)
