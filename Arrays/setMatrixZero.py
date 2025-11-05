class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m  = len(matrix)
        n = len(matrix[0])
        zeroRows = set()
        zeroCols = set()

        #record the position of the 0s in the matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)

        # apply the 0s 
        for i in range(m):
            for j in range(n):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0

                    

