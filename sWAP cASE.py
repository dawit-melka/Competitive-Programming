def swap_case(s):
    arr = list(s)
    for i in range(len(arr)):
        if arr[i].islower():
            arr[i] = arr[i].upper()
        else:
            arr[i] = arr[i].lower()
    return "".join(arr)
