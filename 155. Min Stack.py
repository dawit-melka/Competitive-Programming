# Approach: 1
class Node:
    def __init__(self, currVal, minVal):
        self.val = currVal
        self.next = None
        self.min = min(currVal, minVal)

class MinStack:
    def __init__(self):
        self.first = None
        self.size = 0

    def push(self, val: int) -> None:
        if self.size:
            newNode = Node(val, self.first.min)
            newNode.next = self.first
            self.first = newNode
        else:
            self.first = Node(val, val)
        
        self.size += 1

    def pop(self) -> None:
        self.size -= 1
        self.first = self.first.next
        
    def top(self) -> int:
        return self.first.val

    def getMin(self) -> int:
        return self.first.min
        

# Approach: 2
class MinStack:
    def __init__(self):
        self.stack = []
        self.decending = []

    def push(self, val: int) -> None:
        if not self.decending or val < self.decending[-1][0]:
            self.decending.append((val, len(self.stack)))
        self.stack.append(val)

    def pop(self) -> None:
        currVal = self.stack.pop()
        if self.decending[-1][1] == len(self.stack):
            self.decending.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.decending[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
