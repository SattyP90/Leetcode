class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        

        flat = []
        for row in mat:
            for num in row:
                flat.append(num)


        if len(flat) != r * c:
            return mat 


        reshaped = []
        for i in range(r):
            
            row = []
            for j in range(c):
                row.append(flat[i * c + j])
            reshaped.append(row)

        return reshaped




