# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        #create a stack 
        stack = []

        #whi,e loop through linkeed list 
        while head:

            stack.append(head.val)#add item in linked list into the stack
            head = head.next # go to the next item in the linked list

        #set up pointers
        l, r = 0, len(stack) - 1

        #check if the left most and right most are not the same 

        while l < r:
            if stack[l] != stack[r]:
                return False
            #increment the left 
            #decrement the right
            l += 1
            r -= 1

        #if nothing happens meaning all of them are the same return true
        return True

            
        