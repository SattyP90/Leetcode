class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #map values whilst also containing the "less of " orientation for each character
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman = ""
        i = 0
        while num > 0:
            #keep subtracting while we can fit val[i]
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
            i += 1
        return roman