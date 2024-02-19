class MyLinkedList(object):

    def __init__(self):
        self.List = []

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if len(self.List) > index >= 0:
            return self.List[index]
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.List.insert(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.List.append(val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if 0 <= index <= len(self.List):
            self.List.insert(index, val)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if 0 <= index < len(self.List):
            del self.List[index]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
