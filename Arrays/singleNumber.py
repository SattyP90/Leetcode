class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #hash map to store the repeated values 
        hashmap = {}


        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1



        for key in hashmap:
            if hashmap[key] == 1:
                return key


