class MyStack(object):
    
    

    def __init__(self):
        #create a queue
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #add to the queue on the right
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """

        #loop through the queue for every value except last
        for x in range(len(self.queue) - 1):

            a = self.queue.popleft()
            self.push(a)#move from the start to the end of queue 

        #the very last item in the queue get popped (outputtted)
        output = self.queue.popleft()
        return output

        

    def top(self):
        """
        :rtype: int
        """
        #return the last item added to the queue
        return self.queue[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        #check if the list is 0 or not and return a boolean
        
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()