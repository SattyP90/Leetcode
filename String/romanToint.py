class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        tt = 0
        prev_value = 0

        
        for char in reversed(s):
            current = roman[char]
            if current < prev_value:
                tt -= current 
            else:
                tt += current
            prev_value = current

        return tt

