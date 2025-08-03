# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from fractions import gcd

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr = head

        while curr and curr.next:
            a = curr.val
            b = curr.next.val
            gcd_val = gcd(a, b)

            new_node = ListNode(gcd_val)
            new_node.next = curr.next #set the new node at position of the "next node"
            curr.next = new_node #set the current nodes next item 

            
            curr = new_node.next

        return head