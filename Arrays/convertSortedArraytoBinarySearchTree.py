# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """


        if not nums:
            return None #terminating condition for recursion
        
        mid = len(nums) // 2
        
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid]) #slicing number from the start to the just before the index
        root.right = self.sortedArrayToBST(nums[mid+1:]) #from the index to the end
        
        return root
        