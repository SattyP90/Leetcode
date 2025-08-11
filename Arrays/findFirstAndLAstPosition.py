class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    

        out = [-1, -1]  

        i = 0
        while i < len(nums):
            if nums[i] == target:
                if out[0] == -1:  
                    out[0] = i
                out[1] = i 
            i += 1

        return out