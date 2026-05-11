class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """     
            1) Find locations of bad fruit in grid 
            2) Essentially a BFS where our queue is initalized with bad locations 
            3) need to determine when we have no good fruits left 
        """


        # find locations of bad fruit 
        bad_fruit = deque([]) 
        good_fruit = set() 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                curr = grid[i][j]

                if curr == 2:
                    bad_fruit.append((i,j))
                elif curr == 1:
                    good_fruit.add((i,j))
        

        # bfs from each bad fruit location
        minutes = 0 

        while bad_fruit and len(good_fruit) > 0:

            curr_bad_fruit = len(bad_fruit)

            for i in range(0, curr_bad_fruit):

                row, col = bad_fruit.popleft() 

                # check directions for good fruit
                left = col - 1
                if left >= 0 and grid[row][left] == 1:
                    good_fruit.remove((row, left))
                    grid[row][left] = 2
                    bad_fruit.append((row, left))
                
                right = col + 1
                if right < len(grid[0]) and grid[row][right] == 1:
                    good_fruit.remove((row, right))
                    grid[row][right] = 2
                    bad_fruit.append((row, right))
                

                top = row - 1
                if top >= 0 and grid[top][col] == 1:
                    good_fruit.remove((top, col))
                    grid[top][col] = 2
                    bad_fruit.append((top, col))
                
                bottom = row + 1
                if bottom < len(grid) and grid[bottom][col] == 1:
                    good_fruit.remove((bottom, col))
                    grid[bottom][col] = 2
                    bad_fruit.append((bottom, col))
            
            minutes += 1   

        return minutes if not good_fruit else -1
        


