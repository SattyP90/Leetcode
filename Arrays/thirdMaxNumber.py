class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #create a list for no dup and sorted numbers
        nodup= []


        #add numbers in to the list
        for n in nums:
            if n not in nodup:
                nodup.append(n)

        #reverse sort the numbers 
        nodup.sort(reverse = True)


        #index of the last item
        if len(nodup) < 3:
            return nodup[0]  # Return the max value
        else:
            return nodup[2] 


            

