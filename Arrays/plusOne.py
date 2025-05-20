class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """


        def recurse(index):


            #base case if there are no numbers in the digits
            if index < 0:
                digits.insert(0,1)
                return
            
            #if the digit is less then 9 then just add 1 and end the calls
            if digits[index] < 9:
                digits[index] += 1
                return

            #set the last digit to 0 (9+1 = 1"0")
            #and recursive call the next number to the left 
            else:
                digits[index] = 0
                recurse(index - 1)


        #start the recursion using the index as the parameter
        recurse(len(digits) - 1)
        return digits

        