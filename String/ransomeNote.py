from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        

        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char in ransom_count:
            if ransom_count[char] > magazine_count.get(char, 0):
                return False

        return True