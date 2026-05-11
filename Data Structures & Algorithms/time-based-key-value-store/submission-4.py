class TimeMap:
    """
        key --> [(time, value), (time, value)]
            --> when we call get, it should find value assocaited with time stamp that is <= 
            --> we can use binary search rather than linearly looking for this 
    """

    def __init__(self):
        self.mapping = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        values = self.mapping.get(key, None)
        if not values:
            return "" 

        
        # perform binary search on values looking for time stamp <= provided time stamp 
        low = 0 
        high = len(values) - 1 

        while low <= high:

            mid = (low + high) // 2 
            
            # check if less than provided time stamp 
            if values[mid][0] <= timestamp:
                low = mid + 1 
            else:
                high = mid - 1 
        

        return values[high][1] if values[high][0] <= timestamp else "" 
        
