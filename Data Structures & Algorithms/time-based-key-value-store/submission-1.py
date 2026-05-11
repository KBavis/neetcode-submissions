
class TimeMap:


    def __init__(self):
        self.mapping = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [] 
        
        self.mapping[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        # find value assocaited with timestamp <= specified one 

        if key not in self.mapping:
            return "" 
        
        # grab items we will perfrom binary search on
        items = self.mapping[key]
        
        # identify sample space specific to our items 
        low = 0
        high = len(items) - 1

        min_difference = float('inf')
        res = float('inf')

        while low <= high:

            mid = (low + high) // 2

            # extract current time stamp and calcualte total difference
            curr_timestamp = items[mid][0]
            curr_difference = timestamp - curr_timestamp

            if curr_difference == 0:
                # found exact time stamp 
                return items[mid][1] 
            elif curr_difference < 0:
                # found time stamp > timestamp we are searching for 
                high = mid - 1 
            else:
                # found time stamp < timestamp we are searching for, check if its minimum
                if curr_difference < min_difference:
                    min_difference = curr_difference
                    res = mid 

                low = mid + 1 # attempt to minimize difference 
        
        return items[res][1] if res != float('inf') else ""

        
