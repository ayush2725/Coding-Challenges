class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        dummy_node = ListNode(next = head)
        
        len_of_list = 0
        
        curr_node = head
        
        while curr_node != None:
            
            len_of_list += 1
            curr_node = curr_node.next
        
        prev_node = dummy_node
        curr_node = head
        
        for i in range(len_of_list - n):
            
            prev_node = prev_node.next
            curr_node = curr_node.next
        
        prev_node.next = curr_node.next
        
        return dummy_node.next
