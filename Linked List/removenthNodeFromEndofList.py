# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        




        #find the end of the linked list 
        if not head: 
            return None
    
        
        current = head
        i = 1 #number of items in the linked list
        while current.next:   
            current = current.next

            i += 1


        #item to remove
        itemToRemove= i + 1 - n

        #add all items to list except item to remove

        if itemToRemove == 1:
            return head.next

        #build new list skipping itemToRemove
        dummy = ListNode(0)
        new_curr = dummy
        curr = head
        count = 1
        while curr:
            if count != itemToRemove:
                new_curr.next = ListNode(curr.val)
                new_curr = new_curr.next
            curr = curr.next 
            count += 1

        return dummy.next