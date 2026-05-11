class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        min_heap = [] 
        heapq.heappush(min_heap, (grid[0][0],0,0)) # time, i, j
        
        visited = {}

        while min_heap:

            time, i, j = heapq.heappop(min_heap)

            if (i,j) in visited:
                continue 
            
            visited[(i,j)] = time

            # process neighbors 
            if i - 1 >= 0:
                heapq.heappush(min_heap, (max(time, grid[i - 1][j]), i - 1, j))
            
            if i + 1 < len(grid):
                heapq.heappush(min_heap, (max(time, grid[i + 1][j]), i + 1, j))

            if j - 1 >= 0:
                heapq.heappush(min_heap, (max(time, grid[i][j - 1]), i, j -1))
            
            if j + 1 < len(grid[0]):
                heapq.heappush(min_heap, (max(time, grid[i][j + 1]), i, j + 1))
        

        return visited[len(grid) - 1, len(grid) - 1]

            