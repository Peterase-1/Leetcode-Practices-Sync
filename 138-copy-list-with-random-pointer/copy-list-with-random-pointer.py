# Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        current = head
        while current:
            copy = Node(current.val, current.next)
            current.next = copy
            current = copy.next
        
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        current = head
        copy_head = head.next
        
        while current:
            copy = current.next
            current.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            current = current.next
        
        return copy_head