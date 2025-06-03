class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        out = []
        nodup = {}


        for n in nums:
            if n not in nodup:
                nodup[n] = True 
        
        i = 1

        while i <= len(nums):
            if i not in nodup:
                out.append(i)

            i += 1
        
        return out
        


        """
        class Solution(object):
        def findDisappearedNumbers(self, nums):
        
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] *= -1  # mark as seen by making it negative

        out = []
        for i in range(len(nums)):
            if nums[i] > 0:
                out.append(i + 1)  # i + 1 was not seen

        return out

        """