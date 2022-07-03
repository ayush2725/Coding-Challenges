'''
AUthor: Ayush Singh

Question:
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position 
left to position right, and return the reversed list.

Logic:
We'll go to the node just before the node to start reversing from and we'll reverse it just like we revese a full linked list until we reach
the node left + right - 1. Once that is done, the node from which reversing started will be pointing to None and the node until which reversing
happened will be the current node. We'll just adjust their next pointers and we'll be done. We'll also be keeping a dummy node for the case
in which we have to reverse the head as well

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
    def reverseBetween(self, head, left, right):
        
        # The dummy node
        dummy_node = ListNode(next = head)
        
        left_node = dummy_node
        
        # Reaching the node just before the node to start reversing from
        for i in range (left - 1):
            
            left_node = left_node.next
        
        prev_node = None
        curr_node = left_node.next
        
        # Reversing the nodes to be reversed
        for i in range (right - left + 1):
            
            future_node = curr_node.next
            
            curr_node.next = prev_node
            
            prev_node = curr_node
            
            curr_node = future_node
        
        # Adjusting the pointers
        left_node.next.next = curr_node
        
        left_node.next = prev_node
        
        # Returning the head
        return dummy_node.next
