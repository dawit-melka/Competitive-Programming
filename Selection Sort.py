class Solution: 
    def select(self, arr, i):
        # code here 
        min_val = arr[i]
        min_val_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_val_idx = j
        
        return min_val_idx
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            index = self.select(arr, i)
            arr[index], arr[i] = arr[i], arr[index]
