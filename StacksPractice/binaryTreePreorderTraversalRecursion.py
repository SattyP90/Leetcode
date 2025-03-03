# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """


        results = [] # create a results array 

        def preOrder(root): # recursive function 
            if not root: # if the root is empty end recursion 
                return

            results.append(root.val) #get val of current root 
            preOrder(root.left) #travel to the left branch
            preOrder(root.right) # travel right branch 
        

        preOrder(root) # run recursion 

        return results #  return the results 

