#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        current = i
        while current < n:
            left_idx = 2*current + 1
            right_idx = 2*current + 2
            large_child = current
    
            if left_idx < n and arr[left_idx] > arr[large_child]:
                large_child = left_idx
            if right_idx < n and arr[right_idx] > arr[large_child]:
                large_child = right_idx
    
            if large_child != current:
                arr[current], arr[large_child] = arr[large_child], arr[current]
                current = large_child
            else:
                break
            
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n-1, -1, -1):
            self.heapify(arr, n, i)
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        
        for i in range(n-1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends