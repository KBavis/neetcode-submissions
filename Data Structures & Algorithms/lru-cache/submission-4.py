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

        self.LRU = Node(-1, -1) 
        self.MRU = Node(-1, -1)
        self.LRU.next_node = self.MRU 
        self.MRU.prev = self.LRU 
    
    def add(self, node):
        
        prev = self.MRU.prev 

        node.next_node = self.MRU 
        self.MRU.prev = node 

        prev.next_node = node 
        node.prev = prev 

    def remove(self, node):

        prev_node = node.prev 
        next_node = node.next_node 

        prev_node.next_node = next_node 
        next_node.prev = prev_node


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1 
        
        node = self.cache[key]

        self.remove(node)
        self.add(node)

        return node.val 
        

    def put(self, key: int, value: int) -> None:

        # check if the key already exists 
        if key in self.cache:
            node = self.cache[key]
            del self.cache[node.key]
            self.remove(node)
        
        # check if the capacity is exceeding 
        if len(self.cache) >= self.capacity:

            node_to_remove = self.LRU.next_node
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]
        

        # re-add to linked list and cache 
        node = Node(key=key, val=value)
        self.add(node)
        self.cache[key] = node 
        
