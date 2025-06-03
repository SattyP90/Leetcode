class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = 0 #max
        nm = 0 #new max

        for i in range (len(nums)):


            if nums[i] == 1:
                nm += 1
                if nm > m:
                    m = nm

                    
            else:
                nm = 0

        
        return m
