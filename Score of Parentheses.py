class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for curr in s:
            if curr == "(":
                stack.append(curr)
                continue
                
            curr_sum = 0
            if stack[-1] == "(":
                stack.pop()
                curr_sum = 1
                if stack and stack[-1] != "(":
                    curr_sum += stack.pop()
            else:
                curr_sum = 2*stack.pop()
                stack.pop()
                if stack and stack[-1] != "(":
                    curr_sum += stack.pop()
            stack.append(curr_sum)
        
        return stack[-1]
