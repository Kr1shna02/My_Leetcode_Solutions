class FrontMiddleBackQueue(object):

    def __init__(self):
        self.queue=[]

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.queue.insert(0,val)

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        l=len(self.queue)
        if l%2==0:
            l=l/2
            self.queue.insert(l,val)
        else:
            l=l//2
            self.queue.insert(l,val)       

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.queue.append(val)

    def popFront(self):
        """
        :rtype: int
        """
        if not(len(self.queue)==0):
            return self.queue.pop(0)
        return -1


    def popMiddle(self):
        """
        :rtype: int
        """
        if not(len(self.queue)==0):
            l=len(self.queue)
            if l%2==0:
                l=l/2-1
                return self.queue.pop(l)
            else:
                l=l//2
                return self.queue.pop(l)
        return -1

    def popBack(self):
        """
        :rtype: int
        """
        if not(len(self.queue)==0):
            return self.queue.pop(-1)        
        return -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()