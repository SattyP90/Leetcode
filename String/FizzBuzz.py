class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        i = 1

        out = []

        while i <= n:

            if i % 3 == 0 and i % 5 == 0:
                out.append("FizzBuzz")

            elif i % 3 == 0 :
                out.append("Fizz")

            elif i % 5 == 0:
                out.append("Buzz")

            else:
                out.append(str(i))

            i += 1

        return out
