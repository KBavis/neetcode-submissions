class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        # find all locations of treasure 
        treasure = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]

                if curr == 0:
                    treasure.append((i, j))

        self.INF = 2147483647

        # bfs from these locations 
        distance = 1
        while treasure:

            length = len(treasure)

            # try and reach all "lands" in fewest number of expansions 
            for i in range(length):

                row, col = treasure.popleft() 

                # add transversable positions to queue and modify any land masses found 

                left = col - 1 
                self.search(row, left, grid, treasure, distance)
                
                right = col + 1 
                self.search(row, right, grid, treasure, distance)

                top = row - 1 
                self.search(top, col, grid, treasure, distance)

                down = row + 1 
                self.search(down, col, grid, treasure, distance)

            

            distance += 1 
        
        
    

    def search(self, row, col, grid, q, distance):
        if (
            row < 0 or col < 0 or 
            row >= len(grid) or col >= len(grid[0]) 
            or grid[row][col] != self.INF
        ):
            return 
        
        
        grid[row][col] = distance 
        q.append((row, col))
        


