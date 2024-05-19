class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k):
        self.size = k
        self.capacity = 0
        self.head = None
    
    def enQueue(self, value):
        if self.capacity >= self.size:
            return False
        n = Node(value)
        self.capacity += 1
        if self.head is None:
            self.head = n
            n.next = self.head
            return True
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = n
        n.next = self.head
        return True
    
    def deQueue(self):
        if self.capacity == 0:
            return False
        if self.capacity == 1:
            self.head = None
            self.capacity -= 1
            return True
        last = self.head
        while last.next != self.head:
            last = last.next
        self.head = self.head.next
        self.capacity -= 1
        last.next = self.head
        return True
    
    def Front(self):
        if self.capacity == 0:
            return -1
        return self.head.val
    
    def Rear(self):
        if self.capacity == 0:
            return -1
        last = self.head
        while last.next != self.head:
            last = last.next
        return last.val
    
    def isEmpty(self):
        return self.capacity == 0
    
    def isFull(self):
        return self.capacity == self.size
