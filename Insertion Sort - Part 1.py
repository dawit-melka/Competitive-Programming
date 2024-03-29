#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    # Write your code here
    curr_idx = n-1
    curr_val = arr[curr_idx]
    
    while curr_idx > 0 and curr_val < arr[curr_idx-1]:
        arr[curr_idx] = arr[curr_idx-1]
        print(*arr)
        curr_idx -= 1
    
    arr[curr_idx] = curr_val
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
    print(*arr)
