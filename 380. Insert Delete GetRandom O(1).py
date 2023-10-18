class RandomizedSet:

    def __init__(self):
        self.indexMap = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.indexMap:
            return False
        self.indexMap[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexMap:
            return False
        idx = self.indexMap[val]
        del self.indexMap[val]
        if idx != len(self.values)-1:
            self.values[idx] = self.values[-1]
            self.indexMap[self.values[idx]] = idx
        self.values.pop()
        return True

    def getRandom(self) -> int:
        idx = randint(0, len(self.values)-1)
        return self.values[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
