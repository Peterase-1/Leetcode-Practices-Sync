# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        before = ListNode(0)   
        after = ListNode(0)    
        
        before_tail = before
        after_tail = after
        
        current = head
        
        while current:
            if current.val < x:
                before_tail.next = current
                before_tail = before_tail.next
            else:
                after_tail.next = current
                after_tail = after_tail.next
            current = current.next
        
        
        after_tail.next = None
        
        
        before_tail.next = after.next
        
        return before.next