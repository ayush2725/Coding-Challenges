'''
Author: Ayush Singh

Question:
Given the head of a linked list, rotate the list to the right by k places.
1 -> 2 -> 3 -> 4 -> 5 rotated by 2 places: 4 -> 5 -> 1 -> 2 -> 3

Logic:
Rotating by k places means reaching (k - 3)th node from the end, taking the remaining list, and putting it in front of the 
remaining list. Node: k can be larger than length, so we'll take k % length. There are two corner cases, when len % k == 0,
in that case, we'll return the head. When the list is empty, we'll return None.

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
  
    def rotateRight(self, head, k):
        
        # Case when list is empty
        if head == None:
            return head
        
        len_of_list = 1
        
        curr_node = head
        
        # Calculating length of list
        while curr_node.next != None:
            len_of_list += 1
            curr_node = curr_node.next
        
        sec_node = head
        
        # Case when k % len == 0
        if (k % len_of_list == 0):
            return head
        
        # Reaching the (k-3)th node
        for i in range (len_of_list - (k % len_of_list) - 1):
            
            sec_node = sec_node.next
        
        # Changing the pointers
        curr_node.next = head
        head = sec_node.next
        sec_node.next = None
    
        return head
