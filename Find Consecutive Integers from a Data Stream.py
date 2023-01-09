class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 1
        
    def consec(self, num: int) -> bool:
        if num != self.value:
            self.count = 1
            return False
        if self.count == self.k:
            return True
        
        self.count += 1
        return False
  
