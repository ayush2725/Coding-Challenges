'''
Author: Ayush Singh

Question:
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Logic: 
We'll be having two pointers, a fast pointer and a slow pointer. For simplicity, we've made a dummy node which points to head so that we never have head
as None. Slow pointer will start from dummy node and the fast pointer will start from head. If the value at fast pointer is equal to the value we
want to remove, we set slow pointer equal to next of fast pointer and increment the fast pointer. Else, we increment both slow and fast pointers. At last.
we return the node next to the dummy node

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
    def removeElements(self, head, val):
        
        # Creating the dummy node
        dummy_node = ListNode(next = head)
        
        # Creating the slow and fast pointers
        slow_pointer = dummy_node
        fast_pointer = head
        
        # Iterating until the end of the list
        while fast_pointer != None:
            
            # Case when value is found
            if fast_pointer.val == val:
                
                slow_pointer.next = fast_pointer.next
                fast_pointer = fast_pointer.next
            
            else:
                
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
        
        # Returning the head
        return dummy_node.next
