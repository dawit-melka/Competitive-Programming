class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        for i in range(len(arr)-1, 0, -1):
            sub_arr = arr[:i+1]
            max_val = max(sub_arr)
            max_idx = arr.index(max_val)
            
            if max_idx == i:
                continue
            if max_idx == 0:
                sub_arr.reverse()
                arr = sub_arr  + arr[i+1:]
                result.append(i+1)
            else:
                sub_arr1 = arr[:max_idx+1] 
                sub_arr1.reverse()
                arr = sub_arr1 + arr[max_idx+1:]
                result.append(max_idx+1)
                
                sub_arr2 = arr[:i+1]
                sub_arr2.reverse()
                arr = sub_arr2 + arr[i+1:]
                result.append(i+1)
        
        return result
