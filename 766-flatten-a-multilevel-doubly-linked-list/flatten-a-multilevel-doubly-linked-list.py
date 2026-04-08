class Solution(object):
    def flatten(self, head):
        if not head:
            return head
        
        def dfs(node):
            current = node
            last = None
            
            while current:
                next_node = current.next
                
                if current.child:
                    child_head = current.child
                    child_tail = dfs(child_head)
                    
                    current.next = child_head
                    child_head.prev = current
                    
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
                    
                    current.child = None
                    
                    last = child_tail
                else:
                    last = current
                
                current = next_node
            
            return last
        
        dfs(head)
        return head