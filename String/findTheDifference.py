
from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        #get the count from each count
        countS = Counter(s)
        countT = Counter(t)

        for c in countT: # iterate over the countT 
            if countT[c] > countS.get(c, 0): #check if the count for a character is greater in t than in s
                return c #return the character if the count is high 