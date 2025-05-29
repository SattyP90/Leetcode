class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        #sort the numbers 
        sortedNums = sorted(nums)


        
        #loop through the list 
        for i in range(len(nums)):
            #if the index doesnt match the value in sortedNums
            if (sortedNums[i] != i):
                #return the index which is the missing one
                return i
        
        #return n which would be the missing number 
        return len(nums) 


        


    """

        n = len(nums)
        expectedsum = n * (n + 1) // 2
        actualsum = sum(nums)
        return expectedsum - actualsum
    
    """