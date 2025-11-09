class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        for r in range(9):#iterate through the board 
            for c in range(9):

                #get the val 
                val = board[r][c]

                if val == ".": #if its a empty slot then continue 
                    continue 


                indexBox = (r//3) * 3 + (c//3) #get the index of the box
                
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[indexBox]): #check if the val exists in any of the hashmap in that specific set 
                    return False



                #add the value to the correct map and set 
                rows[r].add(val)
                cols[c].add(val)
                boxes[indexBox].add(val)

            


        return True 
