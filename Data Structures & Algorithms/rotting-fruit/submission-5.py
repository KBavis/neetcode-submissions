class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
            1) find locations of bad fruit 
            2) add these locations to a queue 
            3) expand from each of thos locations in a single MINUTE and add its "expansion"
            4) set of visited location to ensure we don't transverse back to previously seen location
            5) iterate while additional locations in q 
            6) return the total number of miniutes if we foun all locations of fresh fruit  
        """

        q = deque([]) 
        good_fruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    good_fruit += 1

                if grid[i][j] == 2:
                    q.append((i,j))
        

        # NOTE: Instead of having a set of previously seen locations, we can simply change these values to a 
        # "rotten fruit" to ensure we don't reprocess 

        num_minutes = 0
        while q:

            length = len(q)
            for i in range(len(q)):

                row, col = q.popleft()

                # check if this is a "good fruit gone bad"
                if grid[row][col] == 1:
                    good_fruit -= 1 

                # update location to be "rotten" in order to not re-process
                grid[row][col] = 2 

                # process neighbors 
                self.process_neighbors(grid, q, row, col, good_fruit)
            
            if q:
                num_minutes += 1 
        

        # ensure that the total number fruit is equal to zero (meaning we've processed everything)
        return -1 if good_fruit > 0 else num_minutes 
    

    def process_neighbors(self, grid, q, row, col, good_fruit):
        
        # check left 
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            q.append((row, col - 1))

        # check right 
        if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
            q.append((row, col + 1))

        # check up 
        if row + 1 < len(grid) and grid[row + 1][col] == 1:
            q.append((row + 1, col))

        # check down
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            q.append((row - 1, col)) 

        