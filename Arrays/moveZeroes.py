class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p = 0

        #iterate over the list 
        for i in range(len(nums)):


            #if the number isnt a zero move to the front 
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1

        #add the rest of the zeros so it matches the orignal lenght 
        while p < len(nums):
            nums[p] = 0
            p += 1

        