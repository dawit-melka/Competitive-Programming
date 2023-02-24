class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(val2, val1, op):
            if op == "+":
                return val1 + val2
            elif op == "-":
                return val1 - val2
            elif op == "*":
                return val1 * val2
            else:
                if val1 * val2 < 0:
                    return ceil(val1 / val2)
                else:
                    return floor(val1 / val2)

        stack = []
        
        for curr in tokens:
            if curr in ['+', '-', '*',  '/']:
                val1 = stack.pop()
                val2 = stack.pop()
                curr_res = calculate(val1, val2, curr)
                stack.append(curr_res)
            else:
                stack.append(int(curr))
        
        return stack.pop()
