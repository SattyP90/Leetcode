# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        #base case
        if not root:
            return 0


        #recursive calls check left and right nodes and plus 1 each time 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))