class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        


        out = []


        hmap = {}

        for n in nums:
            if n not in hmap:
                hmap[n] = 1
            else:
                hmap[n] += 1


        while k > 0:
            
            max_key = max(hmap, key=hmap.get)
            out.append(max_key)
            del hmap[max_key]
            k -= 1

        
        return out