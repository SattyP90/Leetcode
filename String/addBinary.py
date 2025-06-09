class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        #convert binary string to decimal value
        total = int(a, 2) + int(b ,2)


        #convert decimal to binary and remove the first 2 values 
        return bin(total)[2:]
        