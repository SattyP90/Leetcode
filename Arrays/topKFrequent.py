class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

        #list to add outputs to 
        out = []

        #hashmap to store the coutn of the each number
        hmap = {}


        #iterate over the list and add new new items or increase the count of items
        for n in nums:
            if n not in hmap:
                hmap[n] = 1
            else:
                hmap[n] += 1



        #loop to get the k top frequent nums 
        while k > 0:
            
            #get the key with max values
            max_key = max(hmap, key=hmap.get)

            #add the max key to the output list
            out.append(max_key)

            #delete the max from the map for the next iteration
            del hmap[max_key]
            k -= 1 #decrease k by one for the next iteration

        #return the output list
        return out