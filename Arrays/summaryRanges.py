class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        #list to input the ranges into and return at the end 
        out = []


        #an index
        i = 0 


        #loops to iterate over the list using the index
        while(i < len(nums)):
            start = i   #keeping track of the starting position of the range


            #if this statement is correct then it means that the range is valid adn the value for i will keep iterating 
            while (i + 1 < len(nums) and nums[i+1] == nums[i] + 1):
                i += 1



            #if the i is unchanged that means the range was only 1 number
            if (start == i):
                out.append(str(nums[i]))#add to the output 
            else:
                #just use the start index and the final index and append the range in the correct formate into the list
                out.append("{}->{}".format(nums[start], nums[i]))

            #move to the next num
            i+= 1

        #return the list at the end 
        return out
            

            