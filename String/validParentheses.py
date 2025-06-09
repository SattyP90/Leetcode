class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = []

        # mapping of closing brackets to their matching opening brackets
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        
        for char in s:
            # if the character is a closing bracket
            if char in bracket_map:

                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
               
                stack.append(char)

        
        return len(stack) == 0