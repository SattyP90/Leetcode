class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        #set the index of the first and last itetms 
        left = 0
        right = len(s) - 1

        #making sure the index of the left isnt higher then the index of the right item
        while left < right:

            #swap the items 
            s[left], s[right] = s[right], s[left]

            #increase the left so it goes up one 
            left += 1
            right -= 1#decrease the right so it goes down the list 


