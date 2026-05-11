class TimeMap:

    def __init__(self):
        self.mapping = {} 
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.mapping:
            self.mapping[key] = [(timestamp, value)]
        else:
            self.mapping[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.mapping:
            return "" 
        

        values = self.mapping[key]

        low = 0 
        high = len(values) - 1 

        while low <= high: 

            mid = (low + high) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp: # check if curr_timestamp <= timestamp 
                low = mid + 1 
            else:
                high = mid - 1 
            
        return values[high][1] if high >= 0 else ""