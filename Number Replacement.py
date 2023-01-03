import sys
input = sys.stdin.readline
            

def main():
    t = int(input())
    for _ in range(t):
        arr_len = int(input())
        nums = list(map(int, input().split()))
        string = input().strip()
        dict = {}
        output = "YES"
        for i in range(arr_len):
            char = string[i]
            num = nums[i]
            if num in dict:
                if char != dict[num]:
                    output = "NO"
                    break
            else:
                dict[num] = char
        
        print(output)
if __name__ == "__main__":
    main()
