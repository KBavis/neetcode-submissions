class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next_node = None 
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {} 

        self.MRU = Node(-1, -1)
        self.LRU = Node(-1, -1)

        self.MRU.prev = self.LRU 
        self.LRU.next_node = self.MRU 

    def add_node(self, node):
        prev = self.MRU.prev 

        prev.next_node = node 
        node.prev = prev 

        self.MRU.prev = node 
        node.next_node = self.MRU 

    def remove_node(self, node):

        prev = node.prev 
        next_node = node.next_node

        prev.next_node = next_node 
        next_node.prev = prev 
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        
        # ensure this node is MRU 
        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)

        return node.val 
        

    def put(self, key: int, value: int) -> None:
        
        # check if this is an update 
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            del self.cache[key]
        

        # evict from cache if needed 
        if len(self.cache) >= self.capacity:
            lru = self.LRU.next_node 
            self.remove_node(lru)
            del self.cache[lru.key]
        
        # add new node 
        node = Node(key, value)
        self.cache[key] = node 
        self.add_node(node)

        
