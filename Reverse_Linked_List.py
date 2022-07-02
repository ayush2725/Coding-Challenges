'''
Author: Ayush Singh

Logic:
We'll be maintaining 3 pointers: previous, current, and future. We will continously set the next of current to previous and we'll be keeping
the future so that the next node is not lost.

Time Complexity: O(n)
Space Complexity: O(1)
'''

# Implementation of the Node Class
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
# Implementation to the solution class
class Solution(object):
    def reverseList(self, head):
        
        # Setting the previous and current pointers
        prev_node = None
        curr_node = head
        
        # Iterating until the end and reversing pointers
        while curr_node != None:
            
            future_node = curr_node.next
            
            curr_node.next = prev_node
            
            prev_node = curr_node
            curr_node = future_node
        
        # Returning the head
        return prev_node
