class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        #hashmaps for each string
        smap = {}
        tmap = {}


        #add each char into corresponding maps
        #if theres a duplicate character then just increment the value by 1
        for c in s:
            if c not in smap:
                smap[c] = True
            else:
                smap[c] += 1
        
        for c in t:
            if c not in tmap:
                tmap[c] = True
            else:
                tmap[c] += 1


        #check if the maps match then
        if smap == tmap:
            return True #return true
        else:
            return False #return false