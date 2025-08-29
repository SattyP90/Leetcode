class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(left, right, s):
            #termination conditon 
            if len(s) == n * 2:
                res.append(s)
                return 

            #making sure numbers of left and right brackets are the same 
            #using recursion to solve problem

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res #output 
            