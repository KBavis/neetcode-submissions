class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        """
            a) find all of the TREASURE chests (i.e 0 values)
            b) add values to a queue so we can process via BFS 
            c) starting point are TREASURE chest locations and we expand outwards and process neighbors 
            d) only locatiosn that should be added to queue are land masses
            e) we update these locations with current "level" in order to effectively mark as visited 
        """

        # init queue
        q = deque([])
        self.INF = 2147483647


        # find treasure chests 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        

        current_level = 0 

        # process queue via BFS 
        while q:

            curr_level_length = len(q)
            for i in range(curr_level_length):

                row, col = q.popleft()

                # only update if we're currently at a LAND MASS
                if grid[row][col] == self.INF:
                    grid[row][col] = current_level
                
                # process neighbors 
                self.process_neighbors(row, col, grid, q)
            

            current_level += 1 
        
    


    def process_neighbors(self, row, col, grid, q):

        if row + 1 < len(grid) and grid[row + 1][col] == self.INF:
            q.append((row + 1, col))
        
        if row - 1 >= 0 and grid[row - 1][col] == self.INF:
            q.append((row - 1, col))

        if col - 1 >= 0 and grid[row][col - 1] == self.INF:
            q.append((row, col - 1))
        
        if col + 1 < len(grid[0]) and grid[row][col + 1] == self.INF:
            q.append((row, col + 1))
