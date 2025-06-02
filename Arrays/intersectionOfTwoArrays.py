class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []
        dupmap = {}


        for n in nums1:
            if n not in dupmap:
                dupmap[n] = True
        
        for n in nums2:
            if n in dupmap and n not in out:
                out.append(n)

        return out