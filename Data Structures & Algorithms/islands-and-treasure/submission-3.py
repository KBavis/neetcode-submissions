class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        CHEST = 0
        WATER = -1 

        ROWS = len(grid)
        COLS = len(grid[0])


        """
            1. Find "chests"
            2. Add these locations to a queue and keep a running track of distance 
            3. Any locations that are == LAND, we add to queue and update to be new distance 
            4. Don't need to keep visited set since we'll just avoid those 
        """

        q = deque([])



        # find chests 
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == CHEST:
                    q.append((i, j))
        


        # process until there's no additional locations to process 
        distance = 0 

        while q: 

            print(f"Current State of Queue: {q}, Current Distance: {distance}")

            length = len(q)
            for i in range(length):

                row, col = q.popleft() 

                # process neighbors 
                if row + 1 < ROWS and grid[row + 1][col] == INF:
                    grid[row + 1][col] = distance + 1 
                    q.append((row + 1, col))
                
                if row - 1 >= 0 and grid[row - 1][col] == INF:
                    grid[row - 1][col] = distance + 1 
                    q.append((row - 1, col))
                
                if col + 1 < COLS and grid[row][col + 1] == INF:
                    grid[row][col + 1] = distance + 1 
                    q.append((row, col + 1))
                
                if col - 1 >= 0 and grid[row][col - 1] == INF:
                    grid[row][col - 1] = distance + 1 
                    q.append((row, col - 1))
             


            distance += 1 