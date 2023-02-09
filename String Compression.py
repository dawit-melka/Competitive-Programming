class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0, 0
        while read < len(chars):
            count = 1
            while read < len(chars)-1 and chars[read] == chars[read+1]:
                count += 1
                read += 1
            chars[write] = chars[read]
            if count > 1:
                count = str(count)
                for digit in count:
                    write += 1
                    chars[write] = digit
            
            write += 1
            read += 1
            
        return write
