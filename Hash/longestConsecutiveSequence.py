class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        

        numSet = set(nums)#add the numbers to a map
        maxL = 0 #var for max len 

        for n in numSet:#iterate over the nums 


            if n - 1 not in numSet:#finding the start of the sequence 
                #if n -1 does exist that means the start of the sequence is further in the list


                current = n #set the start of the order here 
                length = 1 #start counting the len


                while current + 1 in numSet:#check if the next num exists 

                    current += 1 #move to that numbers 
                    length += 1 #add to the lenght 

                maxL = max(maxL, length) #update the maxL to the largest value so far 

        
        return maxL #return maxL
                
                

        