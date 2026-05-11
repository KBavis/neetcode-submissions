class TimeMap:

    def __init__(self):
        self.mapping = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [] 
        
        self.mapping[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.mapping:
            return "" 

        values = self.mapping[key]
        

        min_diff = float("inf") # store the timestamp that is either equal to or closest to timestamp (given its <=)
        closest = float("inf")

        low = 0 
        high = len(values) - 1 


        while low <= high:

            mid = (low + high) // 2 
            if values[mid][0] == timestamp:
                return values[mid][1]
            

            if values[mid][0] <= timestamp:
                # compute closest timestamp 
                if timestamp - values[mid][0] < min_diff:
                    min_diff = timestamp - values[mid][0]
                    closest = mid

                low = mid + 1 
            else:
                high = mid - 1


        return values[closest][1] if min_diff != float('inf') else ""