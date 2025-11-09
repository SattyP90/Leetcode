from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        group = defaultdict(list)

        for w in strs:

            key = ''.join(sorted(w))#create a key for that word (anagrams are all the same if sorted)
            #add the word to the key for that word 
            group[key].append(w)


        return list(group.values())#return just the values and not the key
        
        


            
