class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        


        # base ccase
        # if word1 == word2:
        #     return 0
        # elif word1 and words == "":
        #     return len(word1)
        # elif word2 and word1 == "":
        #     return len(words2)




        #2d array
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)] #+1 for base case


        #fill up the 2d array
        for j in range(len(word2) + 1): 
            cache[len(word1)][j] = len(word2) - j

        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        
        #working backwards 
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j +1], cache[i+1][j+1])


        return cache[0][0]






