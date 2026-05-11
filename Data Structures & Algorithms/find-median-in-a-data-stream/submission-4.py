class MedianFinder:

    def __init__(self):
        self.low_nums = [] # max heap
        self.high_nums = [] # min heap
        

    def addNum(self, num: int) -> None:

        # 1) Add to low nums by default 
        heapq.heappush(self.low_nums, -num) 

        # 2) Ensure lengths don't differ by more than 2 
        if len(self.low_nums) > 1 + len(self.high_nums):
            val = -1 * heapq.heappop(self.low_nums)
            heapq.heappush(self.high_nums, val)
        
        # 3) Ensure low_nums <= high_nums 
        if self.low_nums and self.high_nums and -self.low_nums[0] > self.high_nums[0]:
            val = -1 * heapq.heappop(self.low_nums)
            heapq.heappush(self.high_nums, val)

        # 4) Ensure Balanced 
        if len(self.high_nums) > len(self.low_nums):
            val = heapq.heappop(self.high_nums)
            heapq.heappush(self.low_nums, -val)
        

    def findMedian(self) -> float:

        is_even = (len(self.low_nums) + len(self.high_nums)) % 2 == 0

        return ((-1 * self.low_nums[0]) + self.high_nums[0]) / 2 if is_even else self.low_nums[0] * -1
        
        