class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        digits = [int(d) for d in str(x)]



        left = 0
        right = len(digits) - 1

        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1

        
        reversed_num = int("".join(map(str, digits))) * sign

        
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num