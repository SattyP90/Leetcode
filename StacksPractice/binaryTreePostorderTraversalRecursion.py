# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #create an output array
        output = []

        def postOrder(root):
            if not root:
                return # if the root is empty then end the loop
            else:
                postOrder(root.left) # check the left branch
                postOrder(root.right) # check the right branch
                output.append(root.val) # get the val and add to the array

        #run the recursive function
        postOrder(root)
        
        
        #return the array            
        return output