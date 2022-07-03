'''
Author: Ayush Singh

Question:
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes 
the largest integer less than or equal to x.

Logic:
We'll be keeping 2 pointers, a slow and a fast one. For every one step that slow pointer takes, the fast pointer will take 2 steps, so
when the fast pointer reaches the end of the list, the slow pointer will be at the middle node. We'll remove that. For simplicity, we'll
keep a dummy node pointing to the head, for the case in which we have to remove the head.

Time Complexity: O(n)
Space Complexity: O(1)
'''

# Implementation to the Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
# Implementation to the Solution class
class Solution(object):
    def deleteMiddle(self, head):
        
        # Creating the dummy node
        dummy_node = ListNode(next = head)
        
        # Creating the fast and slow pointers
        slow, fast = dummy_node, dummy_node
        
        # Iterating until the end
        while fast.next != None and fast.next.next != None:
            
            slow = slow.next
            fast = fast.next.next
        
        # Deleting the middle node
        slow.next = slow.next.next
        
        # Returning the head
        return dummy_node.next
