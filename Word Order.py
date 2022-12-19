if __name__ == '__main__':
    n = int(input())
    arr = [input() for i in range(n)]
    first_index = {}
    count = 0
    res = []

    # for i in range(n):
    #     arr.append(input())

    for word in arr:
        if(word in first_index):
            res[first_index[word]] += 1
        else:
            first_index[word] = count
            count += 1
            res.append(1)

    print(count)    
    output = " ".join(map(str, res))
    print(output)
