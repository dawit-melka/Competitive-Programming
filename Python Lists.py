if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        command = input().split()
        task = command[0]
        if task == "insert":
            idx = int(command[1])
            val = int(command[2])
            arr.insert(idx, val)
        elif task == "print":
            print(arr)
        elif task == "remove":
            val = int(command[1])
            arr.remove(val)
        elif task == "append":
            val = int(command[1])
            arr.append(val)
        elif task == "sort":
            arr.sort()
        elif task == "pop":
            arr.pop()
        elif task == "reverse":
            arr.reverse()
            
