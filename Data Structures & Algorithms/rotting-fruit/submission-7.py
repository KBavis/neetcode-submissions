class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
            Over unit of time, it's a BFS style problem 
                --> i.e for every FreshFruit adjacent to the rotten fruit, is spread to per unit of time 
            

            1. Find all of the rotten fruit and add to our queue 
            2. Find all of the fresh fruit and add to our set() 
            3. Process the queue layer by layer 
                --> determine if neighbor is a fresh fruit, if so, remove from set of fresh fruit and "make rotten" (seen)
        """
        
        # constants 
        EMPTY = 0
        FRESH = 1 
        ROTTEN = 2 

        def process_neighbors(row, col, q, fresh_fruit):

            # left neighbor 
            if col - 1 >= 0 and grid[row][col - 1] == FRESH:
                grid[row][col - 1] = ROTTEN 
                fresh_fruit.remove((row, col - 1))
                q.append((row, col - 1))
            
            # right neighbor 
            if col + 1 < len(grid[0]) and grid[row][col + 1] == FRESH:
                grid[row][col + 1] = ROTTEN 
                fresh_fruit.remove((row, col + 1))
                q.append((row, col + 1))

                
            # top neighbor 
            if row - 1 >= 0 and grid[row - 1][col] == FRESH:
                grid[row - 1][col] = ROTTEN 
                fresh_fruit.remove((row - 1, col))
                q.append((row - 1, col))

                
            # bottom neighbor 
            if row + 1 < len(grid) and grid[row + 1][col] == FRESH:
                grid[row + 1][col] = ROTTEN 
                fresh_fruit.remove((row + 1, col))
                q.append((row + 1, col))




        # find fresh and rotten fruit 
        q = deque([])
        fresh_fruit = set() 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == FRESH:
                    fresh_fruit.add((i,j))
                elif grid[i][j] == ROTTEN:
                    q.append((i,j))
        

        print(f"Fresh Fruit: {fresh_fruit}, Rotten Fruit: {q}")


        minutes = 0 
        while q and fresh_fruit:

            curr_q_size = len(q)
            for i in range(curr_q_size):
                
                row, col = q.popleft() 
                
                # process the neighbors 
                process_neighbors(row, col, q, fresh_fruit)


            minutes += 1 
        

        return minutes if not fresh_fruit else -1 





