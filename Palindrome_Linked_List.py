'''
Author: Ayush Singh

Question:
Given the head of a singly linked list, return true if it is a palindrome.

Logic:
Since palindromic things are same when we start from the head or the tail, we will reverse half of the linked list, if the len is even, then, from
len // 2 + 1 and if the lenght is odd, then, from len // 2 + 2. Once half of the linked list is reversed, we'll set our pointers to the head
and the mid of the linked list, and compare if all elements are same

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
  
    def isPalindrome(self, head):
        
        # Case when the linked list is empty
        if head == None:
            return None
        
        # Case when there's only one element
        if head.next == None:
            return head
        
        # Variable to store length of linked list
        len_of_list = 0
        
        curr_node = head
        
        # Finding the length of linked list
        while curr_node != None:
            
            len_of_list += 1
            curr_node = curr_node.next
        
        % Deciding from which element to reverse
        if len_of_list % 2 == 0:
            k = len_of_list // 2
        else:
            k = len_of_list // 2 + 1
        
        left = head
        
        # Reaching an element before the element to reverse
        for i in range(k - 1):
            
            left = left.next
        
        prev = None
        curr = left.next
        
        # Reversing the right-half of linked list
        while curr != None:
            
            fut = curr.next
            
            curr.next = prev
            
            prev = curr
            curr = fut
        
        left.next.next = curr
        
        left.next = prev
        
        # Slow and fast pointers from head and mid
        slow = head
        fast = left.next
        
        # Checking if the linked list is palindromic
        for i in range (len_of_list // 2):
            
            if slow.val != fast.val:
                return False
            
            slow = slow.next
            fast = fast.next
        
        return True 
