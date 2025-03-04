class MyQueue(object):

    def __init__(self):

        #create 2 stacks
        self.stack = []
        self.reverseStack = []




    def push(self, x):
        
        """
        :type x: int
        :rtype: None
        """
 
        #add to the queue on the right
        self.stack.append(x)





    def pop(self):
        """
        :rtype: int
        """

        #chekc if the stack is empty
        if not self.stack:
            
            #if not empty, pop the last item and add to the reverse stack
            while self.stack:
                self.reverseStack.append(self.stack.pop())
        
        
        #return the last item in the reverse stack
        return self.reverseStack.pop()
        


    def peek(self):
        """
        :rtype: int
        """
        #chekc if the stack is empty
        if not self.stack:
            #if not empty, pop the last item and add to the reverse stack
            while self.stack:
                self.reverseStack.append(self.stack.pop())
                
            return self.reverseStack[-1]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0 and len(self.reverseStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()