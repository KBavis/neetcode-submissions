class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.next = None 
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {} 

        self.LRU = Node(-1, -1)
        self.MRU = Node(-1, -1)

        self.MRU.prev = self.LRU 
        self.LRU.next = self.MRU 
    

    def add_node(self, node):
        
        prev_node = self.MRU.prev 

        node.next = self.MRU 
        node.prev = prev_node 

        prev_node.next = node 
        self.MRU.prev = node 

    def remove_node(self, node):

        prev_node = node.prev 
        next_node = node.next 

        prev_node.next = next_node
        next_node.prev = prev_node 


    def get(self, key: int) -> int:
        if key not in self.mapping: 
            return -1 
        

        node = self.mapping[key]

        self.remove_node(node)
        self.add_node(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:

        # remove node if this an update 
        if key in self.mapping:
            node = self.mapping[key]
            self.remove_node(node)
            del self.mapping[key]
        

        # evict if capacity reach 
        if len(self.mapping) == self.capacity:
            node = self.LRU.next 
            self.remove_node(node)
            del self.mapping[node.key]
        

        node = Node(key, value)
        self.mapping[key] = node 

        self.add_node(node)

        
