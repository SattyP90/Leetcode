# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def inOrder(root):
            if not root:
                return #return if root empty
            else:
                inOrder(root.left) #go through the left side of the tree
                result.append(root.val) # at the end of the branch add the 
                inOrder(root.right) #then check the right side of the tree and each branch 
        
        inOrder(root) #start the function 

        return result # return result when 