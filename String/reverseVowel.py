class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowelset = set("aeiouAEIOU")
        s = list(s)
        left = 0 
        right = len(s) -1


        while left < right:
            while left < right and s[left] not in vowelset:
                left += 1
            while left < right and s[right] not in vowelset:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)