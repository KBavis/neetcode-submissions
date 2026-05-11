
class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next = None 
        self.prev = None

class LRUCache:
    """
        Idea:
            a) leverage a hash map for quick retireval 
            b) leverage a linked list for optimal insertion and optimal removals when we exceed limit 
            c) use a global capabity to ensure our number of nodes never exceeds specified amount 
            d) need way of determining which nodes is least / most recently used 
                    this is where linked list comes into play
    """
        

    def __init__(self, capacity: int):
        self.capacity = capacity 
        
        self.LRU = Node(-1, -1)
        self.MRU = Node(-1, -1)
        self.LRU.next = self.MRU 
        self.MRU.prev = self.LRU 
        self.mapping = {} 


    def add_node(self, node):

        prev = self.MRU.prev 

        # update node pointers 
        node.prev = prev 
        node.next = self.MRU 

        # update prev and MRU pointers
        self.MRU.prev = node 
        prev.next = node

    

    def remove_node(self, node):

        # grab previous and next node corresponding to specified node 
        prev_node = node.prev 
        next_node = node.next 

        # skip over node being removed (i.e no longer referenced )
        prev_node.next = next_node 
        next_node.prev = prev_node 


    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1 
        

        node = self.mapping[key]

        # remove node from linked list 
        self.remove_node(node)

        # add node back to linked list so it's MRU 
        self.add_node(node)

        return node.val 
        

    def put(self, key: int, value: int) -> None:
        
        # check if the key already exists (i.e if its an update) and remove if so
        if key in self.mapping:
            node = self.mapping[key]
            self.remove_node(node)
            del self.mapping[key]

        # check if cache at capacity 
        if len(self.mapping) >= self.capacity:
            node_to_evict = self.LRU.next 
            del self.mapping[node_to_evict.key]
            self.remove_node(node_to_evict)

        # add node to linked list 
        node = Node(key=key, val=value)
        self.add_node(node)

        # add node to mapping 
        self.mapping[key] = node

        
