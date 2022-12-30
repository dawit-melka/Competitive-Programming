class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        look = False
        temp = ""
        for command in source:
            if not look:
                temp = ""
            n = len(command)
            i = 0
            while i < n:
                if not look:
                    if i+1 < n and command[i] == "/" and command[i+1] == "/":
                        break
                    elif i+1 < n and command[i] == "/" and command[i+1] == "*":
                        i += 2
                        look = True
                    else:
                        temp += command[i]
                        i += 1
                else:
                    if i+1 < n and command[i] == "*" and command[i+1] == "/":
                        look = False
                        i += 2
                    else: 
                        i += 1
            
            if not look and len(temp) > 0:
                res.append(temp)      

        return res
