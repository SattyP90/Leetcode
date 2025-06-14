class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        t_to_s = {}

        for chs, cht in zip(s, t):
            if (chs in s_to_t and s_to_t[chs] != cht) or (cht in t_to_s and t_to_s[cht]!= chs):
                return False
            s_to_t[chs] = cht
            t_to_s[cht] = chs

        return True
            