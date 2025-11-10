class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        out = 0 #output 

        l = 0
        r = 0

        while r < len(nums) - 1:

            far = 0

            for i in range(l , r +1):
                far = max(far, i + nums[i])

            l = r + 1
            r = far 
            out += 1

        return out 






