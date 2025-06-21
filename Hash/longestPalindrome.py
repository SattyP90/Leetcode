class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dupmap = {}
        for l in s:
            if l not in dupmap:
                dupmap[l] = 1
            else:
                dupmap[l] += 1
        
        #return max(dupmap.values())
        out = 0
        odd_found = False

        for count in dupmap.values():
            if count % 2 == 0:
                out += count
            else:
                out += count - 1
                odd_found = True
        
        if odd_found:
            out += 1  

        return out

