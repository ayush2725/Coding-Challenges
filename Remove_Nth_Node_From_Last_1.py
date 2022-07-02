'''
Author: Ayush Singh

Question:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Logic: 
We Iterate through the whole linked list to get the length. We then start iterating again from the head to get to the node before the node we want to delete.
We then set that node's next pointer to the next to next node.

To Save ourselves from corner case of deleting the head by creating a dummy node so that the head never becomes None

Time complexity: O(n)
Space complexity: O(1)
'''

# Implementation to the Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Implementation to the solution
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        # Creating the dummy node pointing to head
        dummy_node = ListNode(next = head)
        
        # Variable to store the length of the list
        len_of_list = 0
        
        
        curr_node = head
        
        # Iterating until end to get the length of list
        while curr_node != None:
            
            len_of_list += 1
            curr_node = curr_node.next
        
        # Pointers to get to node to get deleted
        prev_node = dummy_node
        curr_node = head
        
        # Reaching the node before the node to be deleted
        for i in range(len_of_list - n):
            
            prev_node = prev_node.next
            curr_node = curr_node.next
        
        # Deleting the node
        prev_node.next = curr_node.next
        
        # Returning the head of new list
        return dummy_node.next
