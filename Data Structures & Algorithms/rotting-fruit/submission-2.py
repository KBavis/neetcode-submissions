class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        visited = set()
        bad_fruit_queue = deque() 

        # find positions of fresh and bad fruit 
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                curr = grid[i][j]
                
                if curr == 1:
                    visited.add((i, j))
                if curr == 2:
                    bad_fruit_queue.append((i,j))
        
        # 1) don't want to navigate back to previously processed bad_fruit OR fresh_fruit 
        # 2) we need to know if we processed all fresh_fruit avaialble (if not, we return -1)

        # as of this point, fresh_fruit set contains all areas we hope to reach via BFS 
        minutes = 0 
        while bad_fruit_queue:

            curr_len = len(bad_fruit_queue)
            for i in range(curr_len):

                row, col = bad_fruit_queue.popleft() 

                print(f"Row:{row}, Col:{col}")

                # check left 
                left = col - 1
                if left >= 0 and grid[row][left] == 1 and (row,left) in visited:
                    visited.remove((row, left))
                    bad_fruit_queue.append((row, left))
                
                # check right
                right = col + 1
                if right < len(grid[0]) and grid[row][right] == 1 and (row,right) in visited:
                    visited.remove((row, right))
                    bad_fruit_queue.append((row, right))

                # check bottom
                bottom = row + 1
                if bottom < len(grid) and grid[bottom][col] == 1 and (bottom,col) in visited:
                    visited.remove((bottom, col))
                    bad_fruit_queue.append((bottom, col))
                

                # check up
                up = row - 1
                if up >= 0 and grid[up][col] == 1 and (up,col) in visited:
                    visited.remove((up, col))
                    bad_fruit_queue.append((up, col))
        

            # check if we have discovered all fresh fruit 
            if bad_fruit_queue:
                minutes += 1 
        

        return -1 if len(visited) > 0 else minutes