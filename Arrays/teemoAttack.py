class Solution(object):
    def findPoisonedDuration(self, nums, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        #total hit counter
        hits = 0

        #loop through the nums
        for i in range(len(nums) -1 ):
            #check if the difference between the items in the list 
            #if the difference is greater then the duration then just add the hits      without needing to reset the poison dmg

            if i + 1 < len(nums) and nums[i+1] - nums[i] >= duration:
                hits += duration

            #or else just the hits that would happen before the reset
            else:
                hits += nums[i+1] - nums[i]


        #final item in the list add full duration of the poison
        if nums:
            hits += duration

        #return the hits 
        return hits