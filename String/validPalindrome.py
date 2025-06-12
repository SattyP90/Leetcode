class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #lowercase the s 
        s = s.lower()
        #remove the spaces an punctuation
        s = ''.join(c for c in s if c.isalnum())

        #check if the new s is the same as the reverse of itself
        if s == s[:: -1]:
            return True #return true is yes
        else:
            return False #return false if not 
