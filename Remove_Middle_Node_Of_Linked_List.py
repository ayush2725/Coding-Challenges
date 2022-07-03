# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteMiddle(self, head):
        
        dummy_node = ListNode(next = head)
        
        slow, fast = dummy_node, dummy_node
        
        while fast.next != None and fast.next.next != None:
            
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        
        return dummy_node.next
