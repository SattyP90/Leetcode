# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            #nodes to swap
            first = head
            second = head.next

            #swap
            prev.next = second
            first.next = second.next
            second.next = first

            #move pointers forward
            prev = first
            head = first.next

        return dummy.next