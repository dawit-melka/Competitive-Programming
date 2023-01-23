import sys
import math
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().strip().split()))
        nums.sort()
        result = "YES"
        for i in range(1, n):
            if nums[i] - nums[i-1] > 1:
                result = "NO"
                break
        
        print(result)



if __name__ == "__main__":
    main()
