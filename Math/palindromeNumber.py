class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digits = [str(d) for d in str(x)]

        right = len(digits) -1 
        left = 0

        out = True

        while left < right:
            if digits[left] != digits[right]:
                return False  
            left += 1
            right -= 1

        return True



            



        