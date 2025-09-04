# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

        curr = head

        while curr and curr.next:

            if curr.val == curr.next.val: #check if the value are the sames
                curr.next = curr.next.next #remove the duplicate item with the item to the right of it 
            else:
                curr = curr.next 

        return head #return the head 