class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        right = 0

        while right < len(path):
            char = path[right]
            if stack[-1] == char == "/":
                right += 1
                continue
            
            left = right
            while right < len(path) and path[right] != "/":
                right += 1

            file_name = path[left: right]
            if file_name == "..":
                if len(stack) > 1:
                    stack.pop()
                    stack.pop()
            elif file_name != ".":
                stack.append(file_name)
                stack.append("/")
        
        if len(stack) > 1:
            stack.pop()

        return "".join(stack)
            
            
