class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
    
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        rows = rowIndex

        triangle = []


        for i in range (rows + 1):
            row = [1] * (i+1) #new row with just ones 


            for j in range(1,i): #for the items in a rows (columsn)

            #create the row by adding the correct values top left and directly above
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            #add to the triangle
            triangle.append(row)
    


        
        return triangle[rowIndex]
