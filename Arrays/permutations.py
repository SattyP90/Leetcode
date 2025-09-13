class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        


        if len(nums) == 0:
            return [[]]
        


        perms = self.permute(nums[1:]) #get all values from num except the first 1

        res = [] 


        for p in perms:
            for i in range(len(p) + 1):
                copyp = list(p)

                copyp.insert(i, nums[0])
                res.append(copyp)

        return res