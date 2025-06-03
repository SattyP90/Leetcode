class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        # cookies = {}
        # happy = 0
        # for aCook in s:
        #     if aCook not in cookies:
        #         cookies[aCook] = 1
        #     else:
        #         cookies[aCook] += 1
        # for greed in g:
        #     if greed in cookies:
        #         cookies[greed] -= 1
        #         happy += 1
        # return happy
            
        g.sort()
        s.sort()

        happy = 0
        i = 0

        for greed in g:



            while i < len(s) and s[i] < greed:
                i += 1  

                
            if i < len(s):
                happy += 1
                i += 1  


        return happy


        