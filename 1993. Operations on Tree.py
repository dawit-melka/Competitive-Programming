class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None] * len(self.parent)
        self.children = defaultdict(list)
        for i in range(1, len(parent)):
            self.children[parent[i]].append(i)
        

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] =None
        return True
        

    def upgrade(self, num: int, user: int) -> bool:
        currNode = num
        while currNode != -1:
            if self.locked[currNode]:
                return False
            currNode = self.parent[currNode]
        
        hasLockedDescendant= False
        queue = deque([num])
        while queue:
            currNode = queue.popleft()
            if self.locked[currNode]:
                hasLockedDescendant = True
                self.locked[currNode] = None
            queue.extend(self.children[currNode])

        if hasLockedDescendant:
            self.locked[num] = user

        return hasLockedDescendant
