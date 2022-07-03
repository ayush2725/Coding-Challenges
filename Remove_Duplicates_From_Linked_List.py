'''
Author: Ayush Singh

Question:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Logic:
Using two pointers, slow pointer will be at the head and the fast will be at head.next. While head.next is not None, we'll move the slow pointer and the
fast pointer until both values are not equal, and then change the pointer.

Time Complexity: O(n)
Space Complexity: O(1)
'''

# Implementation to the Node class
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
# Implementation to the Solution Class
class Solution(object):
    def deleteDuplicates(self, head):
        
        # Corner case for when the list is empty
        if head == None:
            return head
        
        # Initializing slow and fast pointers
        slow = head
        fast = head.next
        
        # Iterating until the end of the list
        while fast != None:
            
            # When duplicate is found
            if slow.val == fast.val:
                fast = fast.next
            
            # When duplicate is not found
            else:
                
                slow.next = fast
                
                slow = fast
                fast = fast.next
        
        # Case when there are duplicates at the end
        slow.next = fast
        
        return head
