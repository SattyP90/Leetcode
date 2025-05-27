class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #create a hashmap
        dup = {}

        #add to hash map with a count
        for n in nums:
            if n not in dup:
                dup[n] = 1
            else:
                dup[n] += 1



        #loooking for a count with more than 1 meaning theres a duplicate in the list
        for count in dup.values():
            if count > 1:
                return True #return true

        #if all the counts are 1 then no duplicates are in the list
        return False