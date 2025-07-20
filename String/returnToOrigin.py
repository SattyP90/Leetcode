class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        

        m = list(moves)

        maps = [0,0]
        for c in m:
            if c == "U":
                maps[1] += 1
            if c == "D":
                maps[1] -= 1
            if c == "L":
                maps[0] -= 1
            if c == "R":
                maps[0] += 1 


        if maps == [0,0]:
            return True 
        else:
            return False
                