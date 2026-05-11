class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
            Goal: Find the minimum path that exists to navigat from (0, 0) to (len(grid) - 1, len(grid[0]) - 1)     
                    - The total tiem will essentially just be the last 

            How:
                a) Start at 0,0 
                b) Add neighbors that we can process to minHeap 
                c) Iterate through while minHeap 
        """


        minHeap = [] 
        heapq.heappush(minHeap, (grid[0][0], 0, 0)) 
        processed = set()


        while minHeap: 

            maxSeen, row, col = heapq.heappop(minHeap)
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return maxSeen 
            
            # add current location to proccessed 
            processed.add((row, col))

            # process neighbors 
            self.process_neighbors(row, col, grid, minHeap, maxSeen, processed)
    

    def process_neighbors(self, row, col, grid, minHeap, maxSeen, processed):
        
        # down
        if row + 1 < len(grid) and (row + 1, col) not in processed:
            val = grid[row + 1][col]
            heapq.heappush(minHeap, (max(val, maxSeen), row + 1, col))
        
        # up 
        if row - 1 >= 0 and (row - 1, col) not in processed:
            val = grid[row - 1][col]
            heapq.heappush(minHeap, (max(val, maxSeen), row - 1, col))

        # left 
        if col - 1 >= 0 and (row, col - 1) not in processed:
            val = grid[row][col - 1]
            heapq.heappush(minHeap, (max(val, maxSeen), row, col - 1))

        # right 
        if col + 1 < len(grid[0]) and (row, col + 1) not in processed:
            val = grid[row][col + 1]
            heapq.heappush(minHeap, (max(val, maxSeen), row, col + 1))

