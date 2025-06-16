class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        #split the s into seperate words
        words = s.split()


        #check if the lenght of the word is the same as pattern
        if len(words) != len(pattern):
            return False

        #map out the links between the words
        s_to_p = {}
        p_to_s = {}


        #check the links are correct and there are no different words getting linked 
        for chp, chs in zip(pattern, words):
            if (chs in s_to_p  and s_to_p[chs] != chp) or (chp in p_to_s and p_to_s[chp]!= chs):
                return False
            s_to_p[chs] = chp
            p_to_s[chp] = chs


        #return true if checks pass
        return True