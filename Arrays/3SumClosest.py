class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2] 

        for i in range(len(nums) - 2):  
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                
                if abs(total - target) < abs(res - target):
                    res = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    
                    return target
        
        return res