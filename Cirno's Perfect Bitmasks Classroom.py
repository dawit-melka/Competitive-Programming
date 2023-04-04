t = int(input())

for _ in range(t):
    num = int(input())
    if num == 1:
        print(3)
        continue
    i = 1
    while (num & i) == 0:
        i = i << 1
    while (num ^ i) == 0:
        i += 1
    
    print(i)
