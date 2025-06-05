class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        
        numTypes = len(set(candyType))
        
        eatMax = len(candyType) / 2

        if eatMax >= numTypes:
            return numTypes
        else:
            return eatMax


        
        