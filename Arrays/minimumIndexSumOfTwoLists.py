class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """


        index_map = {}
        for i in range(len(list1)):
            word = list1[i]
            index_map[word] = i

        min_sum = float('inf')
        result = []  

        for j, word in enumerate(list2):
            if word in index_map:
                index_sum = index_map[word] + j
                if index_sum < min_sum:
                    result = [word]
                    min_sum = index_sum
                elif index_sum == min_sum:
                    result.append(word)
        
        return result