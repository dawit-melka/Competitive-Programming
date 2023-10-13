class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.prev = None 
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.first = Node(0, 0)
        self.last = Node(0, 0)
        self.first.next = self.last
        self.last.prev = self.first
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        node.prev = None
        node.next = None
        
    def insert(self, node):
        last = self.last.prev
        last.next = node
        node.prev = last
        node.next = self.last
        self.last.prev = node

    def get(self, key: int) -> int:
        cache = self.cache
        if key not in cache:
            return -1
        currNode = self.cache[key]
        self.remove(currNode)
        self.insert(currNode)
        return currNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.capacity:
            lru = self.first.next
            del self.cache[lru.key]
            self.remove(lru)

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
