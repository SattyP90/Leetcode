class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
        num1 = 0
        num2 = 0

        for num in range(n + 1):
            if num % m == 0:
                num2 += num

            else:
                num1 += num

        return num1 - num2
