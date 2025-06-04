class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #int to be outputted
        out = 0

        #sort the numbers as optimal is to get pairs when they are ordered 
        nums.sort()


        #index for the list 
        i = 0

        #iterate over the sorted nums
        while i < len(nums):
            #check item not out of bounds
            if i < len(nums) - 1:
                out += min(nums[i], nums[i+1])
            
            #increment 2 so it goes to the next pair
            i += 2

        #return the output
        return out