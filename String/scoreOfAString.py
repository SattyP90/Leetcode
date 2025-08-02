class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        #variable to hold the total
        total = 0

        #iterate over the s 
        for i in range (len(s) - 1):
            total += abs(ord(s[i]) - ord(s[i + 1])) #get the ascii value and get the abs val of neighbouring s 


        #return total
        return total 



        