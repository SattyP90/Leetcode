class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        seen = set()
        dup = -1
        
        for n in nums:
            if n in seen:
                dup = n
            seen.add(n)

        n = len(nums)
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [dup, missing]