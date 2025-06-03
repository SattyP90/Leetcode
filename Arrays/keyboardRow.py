class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """


        #output list
        out = []

        #creating sets containing the keyboard rows
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")



        #iterate over the words in the list 
        for w in words:

            lowerW = set(w.lower()) #removes duplicate letter

            #check of the word is within each subset
            if lowerW.issubset(set1) or lowerW.issubset(set2) or lowerW.issubset(set3):
                out.append(w)#if so then add to the list


        return out #return the list