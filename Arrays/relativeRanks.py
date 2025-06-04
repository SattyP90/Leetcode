class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """


        first = "Gold Medal"
        second = "Silver Medal"
        third = "Bronze Medal"

        
        hmap = {}
        for i in range(len(score)):
            hmap[score[i]] = i

        
        sorted_scores = sorted(score, reverse=True)

        out = [0] * len(score)

        for rank, val in enumerate(sorted_scores):
            idx = hmap[val]
            if rank == 0:
                out[idx] = first
            elif rank == 1:
                out[idx] = second
            elif rank == 2:
                out[idx] = third
            else:
                out[idx] = str(rank + 1)

        return out
            

        