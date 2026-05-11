class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nextt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = Node(-1, -1) 
        self.MRU = Node(-1, -1) 
        self.capacity = capacity
        self.mapping = {}

        # setup pointers
        self.LRU.nextt = self.MRU
        self.MRU.prev = self.LRU 

    def add_node(self, node):

        # add at MRU 
        prev_node = self.MRU.prev 

        # update existing pointers
        self.MRU.prev = node 
        prev_node.nextt = node 

        # update new node pointers 
        node.nextt = self.MRU 
        node.prev = prev_node 
    
    def remove_node(self, node):

        prev_node = node.prev 
        next_node = node.nextt 

        prev_node.nextt = next_node 
        next_node.prev = prev_node 

    
    def get(self, key: int) -> int:

        if key not in self.mapping:
            return -1

        node = self.mapping[key]
        self.remove_node(node)
        self.add_node(node)
        return node.value
                 

    def put(self, key: int, value: int) -> None:

        # check if an update 
        if key in self.mapping:
            node_to_delete = self.mapping[key]
            del self.mapping[key]
            self.remove_node(node_to_delete)
        
        # check if at capacity 
        if len(self.mapping) == self.capacity:
            
            # remove LRU 
            node_to_delete = self.LRU.nextt 
            del self.mapping[node_to_delete.key]
            self.remove_node(node_to_delete)
        

        # add node to linked list and mapping 
        new_node = Node(key, value)
        self.mapping[key] = new_node
        self.add_node(new_node)


    
    """

    1. Get 
        - Hashmap (Key, Node)
        - Operation:
            - move to MRU 
            - check if value in hashmap
            - return value in hashap or -1 
    
    2. Put 
        - Add To HashMap 
        
    3. Eviction
        - When Adding "New" Element, Check If Already At Capacity (don't invoke if key already exists)
        - Pointer to LRU and MRU 
    """
        
