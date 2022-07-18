class MyQueue(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        helperStack = []
        
        while self.queue:
            helperStack.append(self.queue.pop())
            
        self.queue.append(x)
        
        while helperStack:
            self.queue.append(helperStack.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()