class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """




        nums.sort()

        i = len(nums) - 1
        first =nums[i]
        second = nums[i-1]
        third = nums[i-2]

        prod1 = first* second * third
        prod2 = nums[0] * nums[1] * nums[-1]


        return max(prod1,prod2)