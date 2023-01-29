class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)

    def get(self, index: int) -> int:
        curr = self.head.next
        for _ in range(index):
            if curr == None:
                return -1
            curr = curr.next
        if curr == None:
            return -1
        return curr.value        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        
        while curr.next:
            curr = curr.next
        curr.next = newNode      

    def addAtIndex(self, index: int, val: int) -> None:        
        newNode = Node(val)
        curr = self.head
        for _ in range(index):
            if curr == None:
                break
            curr = curr.next
        if curr != None:
            newNode.next = curr.next
            curr.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for _ in range(index):
            if curr == None:
                break
            curr = curr.next
        if curr != None and curr.next != None:
            curr.next = curr.next.next
