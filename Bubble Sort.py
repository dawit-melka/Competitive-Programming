import math
import os
import random
import re
import sys

def countSwaps(a):
    # Write your code here
    n = len(a)
    count_swaps = 0
    for l in range(n-1, -1, -1):
        for r in range(l):
            if a[r] > a[r+1]:
                a[r], a[r+1] = a[r+1], a[r]
                count_swaps += 1
    return count_swaps
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    count_swaps = str(countSwaps(a))
    print("Array is sorted in "+count_swaps+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))
