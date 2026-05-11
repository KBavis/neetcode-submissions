class Node:

    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.next = None 
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.MRU = Node(-1, -1)
        self.LRU = Node(-1, -1)

        self.LRU.next = self.MRU 
        self.MRU.prev = self.LRU  
    

    def add(self, node):
        prev_node = self.MRU.prev 

        self.MRU.prev = node 
        prev_node.next = node 

        node.next = self.MRU 
        node.prev = prev_node
    
    def remove(self, node):

        prev_node = node.prev 
        next_node = node.next 

        prev_node.next = next_node 
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        

        node = self.cache[key]

        # remove node & re-add to MRU 
        self.remove(node)
        self.add(node)

        return node.value
        
    def put(self, key: int, value: int) -> None:

        # check if update
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
        
        # check if capacity reached 
        if len(self.cache) >= self.capacity:
            node_to_remove = self.LRU.next 
            del self.cache[node_to_remove.key]
            self.remove(node_to_remove)

        # create new node and add to cache / linked list
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node 








        
