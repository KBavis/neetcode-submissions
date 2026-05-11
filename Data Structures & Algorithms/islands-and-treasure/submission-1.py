class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        queue = deque() 

        INF = 2147483647

        # first find all treasures (starting points)    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        

        # BFS from all treasures simulatenously 
        while queue:
            r, c = queue.popleft() 
            current_distance = grid[r][c]

            # explore right 
            if c + 1 < cols and grid[r][c + 1] == INF:
                grid[r][c + 1] = current_distance + 1
                queue.append((r, c + 1)) 

            # Explore LEFT
            if c - 1 >= 0 and grid[r][c - 1] == INF:
                grid[r][c - 1] = current_distance + 1
                queue.append((r, c - 1))
            
            # Explore DOWN
            if r + 1 < rows and grid[r + 1][c] == INF:
                grid[r + 1][c] = current_distance + 1
                queue.append((r + 1, c))
            
            # Explore UP
            if r - 1 >= 0 and grid[r - 1][c] == INF:
                grid[r - 1][c] = current_distance + 1
                queue.append((r - 1, c))
        


        