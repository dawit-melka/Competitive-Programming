class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque()
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) == self.maxSize:
            return False
        self.queue.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.queue) == self.maxSize:
            return False
        self.queue.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.popleft()
        return True

    def deleteLast(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.pop()
        return True

    def getFront(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def getRear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.maxSize
