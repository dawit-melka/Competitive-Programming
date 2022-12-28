A = input().split()
n = int(input())
set_A = set(A)
size_A = len(set_A)
res = "True"

for i in range(n):
    curr_arr = input().split()
    set_B = set(curr_arr)
    
    if len(set_B) >= size_A:
        res = "False"
        break
    
    for val in set_B:
        if val not in set_A:
            res = "False"
            break
    
    if res == "False":
        break
      
print(res)
