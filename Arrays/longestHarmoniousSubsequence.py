class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        
        maxsize = 0
        newmax = 0
        i = 0

        # while i < len(nums) - 1:
        #     if i < len(nums) - 1 and nums[i+1] - nums[i] == 1:
        #         newmax += 1
        #         i+= 1
        #         if newmax > maxsize:
        #             maxsize = newmax
        #             newmax = 0
        #     elif i < len(nums) - 1 and nums[i +1 ] == nums[i]:
        #         newmax += 1
        #         i+= 1
        #         if newmax > maxsize:
        #             maxsize = newmax
        #             newmax = 0
        #     else:
        #         i+=1
        
        start = 0

        #sliding window method
        #end will go from 0 to the lenght of the nums
        for end in range(len(nums)):
            #while the end index and the start index dont have a difference of 1 then just keep moving up
            while nums[end] - nums[start] > 1:
                start += 1

            if nums[end] - nums[start] == 1:
                maxsize = max(maxsize, end - start + 1)


        return maxsize
                