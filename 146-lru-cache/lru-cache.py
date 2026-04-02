class Node:
    def __init__(self, key, val):
        self.key = key          
        self.val = val          
        self.prev = None        
        self.next = None        


class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity     
        self.cache = {}         

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev            
        nxt = node.next             

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev      
        nxt = self.right            

        prev.next = node            
        node.prev = prev            

        node.next = nxt
        nxt.prev = node             
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]

            self.remove(node)       
            self.insert(node)       

            return node.val

        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)     
        self.cache[key] = node      
        self.insert(node)           

        if len(self.cache) > self.cap:
            lru = self.left.next    
            self.remove(lru)        
            del self.cache[lru.key] 