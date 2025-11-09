class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        rows = [set () for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue 


                indexBox = (r//3) * 3 + (c//3)


                rows[r].add(val)
                cols[c].add(val)
                boxes[indexBox].add(val) 


                #add new numbers 


        def backtrack(r, c):
            if r == 9:
                return True
            
            if c == 9:
                return backtrack(r + 1, 0)
            
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            # Try digits 1–9
            for num in map(str, range(1, 10)):


                indexBox = (r // 3) * 3 + (c // 3)


                if num not in rows[r] and num not in cols[c] and num not in boxes[indexBox]:
                    
                    board[r][c] = num #add the number to the board 


                    #add the number to the maps so its updated
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[indexBox].add(num)

                    #move the next column 
                    if backtrack(r, c + 1):
                        return True

                    #Undo (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[indexBox].remove(num)

            # if no valid numbers work then fail 
            return False
        
        backtrack(0,0)

