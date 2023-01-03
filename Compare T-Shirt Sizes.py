import sys
input = sys.stdin.readline
            

def main():
    t = int(input())
    size_in_num= {"S":0, "M":1, "L":2}
    for _ in range(t):
        sizeA, sizeB = input().split()
        A = len(sizeA)
        B = len(sizeB)
        size_type_A = sizeA[A-1]
        size_type_B = sizeB[B-1]
        compare_result = ""
        if size_in_num[size_type_A] > size_in_num[size_type_B]:
            compare_result = ">"
        elif size_in_num[size_type_A] < size_in_num[size_type_B]:
            compare_result = "<"
        else:
            if A==B:
                compare_result = "="
            elif A > B:
                if size_type_A == "S":
                    compare_result = "<"
                else:
                    compare_result = ">"
            else:
                if size_type_A == "S":
                    compare_result = ">"
                else:
                    compare_result = "<"
        
        print(compare_result)
        
if __name__ == "__main__":
    main()
