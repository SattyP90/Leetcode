class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = {}

        highestk = 0

        for n in nums:
            if n in counter:
                counter[n] += 1 
            #add the value into the map
            else:
                counter[n] = 1

        for key in counter:
            if key > highestk:
                highestk = key



        maxkey = max(counter, key=counter.get)
        return maxkey
