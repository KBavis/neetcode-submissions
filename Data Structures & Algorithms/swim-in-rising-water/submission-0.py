class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
            grid[i][j] = elevant at point i,j

            at time t --> this is water elvel across the entire grid 

            go up/down or left/right IF eleveation of both squares is LESS THAN OR EQUAL TO water level at time t 


            start [0][0] --> reach end [n -1][n - 1] in mimum amount of time 


            canSwim(i,j, t):
                if grid[i][j + 1] <= t --> swim right 
                if grid[i][j - 1] <= t --> swim left 
            

            can only transverse to that cell if t = 
 

            the return will be the maximum time seen on the path 
        """


        
        visited = {}

        heap = [] 
        heapq.heappush(heap, (grid[0][0], 0, 0)) # time, row, col 

        while heap:

            time, row, col = heapq.heappop(heap)

            if (row,col) in visited:
                continue 
            
            visited[(row, col)] = time 
            # process neighbors 

            # up
            if row + 1 < len(grid):
                heapq.heappush(heap, (max(time, grid[row + 1][col]), row + 1, col))
            
            # down 
            if row - 1 >= 0:
                heapq.heappush(heap, (max(time, grid[row - 1][col]), row - 1, col))
            
            # left 
            if col - 1 >= 0:
                heapq.heappush(heap, (max(time, grid[row][col - 1]), row, col - 1))
            
            # right 
            if col + 1 < len(grid[0]):
                heapq.heappush(heap, (max(time, grid[row][col + 1]), row, col + 1))
            
        
        return visited[(len(grid) - 1, len(grid) - 1)]


        
            


