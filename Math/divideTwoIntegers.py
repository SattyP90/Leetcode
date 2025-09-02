class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """


        #signs for each item
        divd_isPos = True
        divs_isPos = True
        

        #base case
        if dividend == 0:
            return 0

        #store the sign 
        if dividend < 0: 
            divd_isPos = False
        if divisor < 0:
            divs_isPos = False


        outSignisPos = False
        if divd_isPos == divs_isPos:
            outSignisPos = True
        

        res = 0

        divd = dividend
        divs = divisor


        while abs(divd) >= abs(divs):
            divd -= divs 
            res += 1

        if outSignisPos:
            return res
        else:

            res = -res
            return res



#seconds solution with no time limit errors    
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """


        
        #edge case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        #work with abs values so no need to worry about negatives 
        a = abs(dividend)
        b = abs(divisor)
        res = 0

        while a >= b:
            temp, multiple = b, 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            res += multiple


        #add the correct signs before return the results 
        if (dividend > 0) == (divisor > 0):
            return res
        else:
            return -res
