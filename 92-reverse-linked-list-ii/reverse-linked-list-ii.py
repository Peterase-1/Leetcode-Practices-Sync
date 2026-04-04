class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        start = prev.next
        then = start.next
        
        for _ in range(right - left):
            start.next = then.next  
            then.next = prev.next  
            prev.next = then        
            then = start.next       
        
        return dummy.next