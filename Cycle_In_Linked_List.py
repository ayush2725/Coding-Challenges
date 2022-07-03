'''
Author: Ayush Singh

Question:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Logic:
We'll be using 2 pointers, a slow and a fast. For one step that the slow pointer takes, the fast pointer will take 2 steps. By logic,
if there is a cycle in the list, then, the slow and fast pointers will collide at some time. If there isn't a cycle, the fast pointer 
will hit None

Time Complexity: O(n)
Space Complexity: O(1)
'''

# Implementation to the Node class
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

# Implementation to the Solution class
class Solution(object):
    def hasCycle(self, head):
        
        # Corner case when list is empty
        if head == None:
            return False
        
        # Initializing slow and fast pointers
        slow_node = head
        fast_node = head.next
        
        while slow_node != fast_node:
            
            # Case when we've hit the end
            if fast_node == None or fast_node.next == None:
                return False
            
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        return True
        
