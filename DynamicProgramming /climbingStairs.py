class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """



        one = 1
        two = 1
        #fibonacci sequence 
        
        for i in range(n - 1):

            temp = one 
            one = one + two 
            two = temp 

        return one 