class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = 0

    def next(self, price: int) -> int:
        self.count += 1
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()

        if not self.stack:
            self.stack.append((price, self.count))
            return self.count
          
        val, prevCount = self.stack[-1]
        self.stack.append((price, self.count))
        
        return self.count - prevCount
    
