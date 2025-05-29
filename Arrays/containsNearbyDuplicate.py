class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #create a set
        seen = set()

        #loops through the list
        for i in range(len(nums)):

            #if the number is in the seen set then return true
            if nums[i] in seen:
                return True
            
            #or just add the number in
            seen.add(nums[i])


            #if the seen lenght is greater then k (meaning numbers are out of the window) then remove them 

            if len(seen) > k :
                seen.remove(nums[i-k])

        return False

        
