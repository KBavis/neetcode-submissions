class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
            1. Need way to track number of "fresh fruit" 
            2. Need way to track which fruits are currently "rotten" 

            - Find where all the rotten fruit are 
                    --> these will be are starting points for our search 
            
            - Find number of fresh fruit 
            - Only able to transverse in a direction that has fresh fruit 
                    --> once we "process" a fresh fruit, it becomes rotten 
                            --> decrement number of fresh fruit 
                            --> mark as "visitied" by changing to a rotten fruit 
        """

        self.ROWS = len(grid)
        self.COLS = len(grid[0])


        # find fresh and rotten fruits 
        self.total_fresh_fruit = 0
        q = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    self.total_fresh_fruit += 1 
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        # no fersh fruit found
        if self.total_fresh_fruit == 0:
            return 0 
        

        # perform BFS from the locations that are rotten fruit 
        time = 0 
        while q: 

            
            print(f"Time: {time}, Num Fresh Fruit: {self.total_fresh_fruit}, Queue: {q}")

            num_fruit = len(q)
            for i in range(num_fruit):

                row, col = q.popleft() 

                # process neighbors if needed 
                self.process_neighbors(row + 1, col, grid, q)
                self.process_neighbors(row - 1, col, grid, q)
                self.process_neighbors(row, col + 1, grid, q)
                self.process_neighbors(row, col - 1, grid, q)
            
            # ensure we don't increment time if we've processed all fruit 
            if not q and self.total_fresh_fruit == 0:
                return time 

            time += 1 
        
        print('HERE')
        print(f"Q: {q}")
        return time if self.total_fresh_fruit == 0 else -1


    def process_neighbors(self, row, col, grid, q):
        if (
            row >= 0 and 
            row < self.ROWS and 
            col >= 0 and 
            col < self.COLS and 
            grid[row][col] == 1
        ):
            self.total_fresh_fruit -= 1 
            grid[row][col] = 2
            q.append((row, col))

