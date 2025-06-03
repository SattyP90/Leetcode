class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        out = []#return output list
        dup = {} #hashmap to store count and duplicate


        # iterate over the list and add new items in the map with a count
        for n in nums1:
            if n not in dup:
                dup[n] = 1

            else:
                dup[n] += 1

        
        #iterate over then next list
        for n in nums2:
            #if the item is in the hashmap and has a counter greater than 0
            if n in dup and dup[n] > 0:
                out.append(n) #add to the list 
                dup[n] -= 1 #reduce the count by one
        
        
        return out #return the final list