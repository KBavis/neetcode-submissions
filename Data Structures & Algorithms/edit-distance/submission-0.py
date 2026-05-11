class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """ 

        We manipulate word 1 to be equivalent to word 2 

        We can 
            a) add a character 
            b) remove a character
            c) replace a character 

        w1 = money
        w2 = mon

        if i == len(w1):
            --> add characters 

        if j == len(w2):
            --> remove characters from i 


        oooh
        hooh

        oooh
        vvvvvvvvvvv

        monkeys 
        money 

        How do we track number of operations:
            this should be what we return up call stack 

        Base Case:
            a) i == len(word1) and j == len(word2):
                return 0 
            b) i == len(word1)

        Case:
            a) w1[i] == w2[j]:
                return dfs(i + 1, j + 1)
            
            b) w1[i] != w2[j]:
                insert_operations = 1 + dfs(i + 1, j + 1)
        """


        memo = {}

        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            elif i == len(word1) and j == len(word2):
                return 0
            

            # handle situatiosn where i == len(word1) --> remove characters 
            if i == len(word1):
                num_operations = 1 + dfs(i, j + 1)
                memo[(i,j)] = num_operations 
                return num_operations
            elif j == len(word2):
                num_operations = 1 + dfs(i + 1, j)
                memo[(i,j)] = num_operations 
                return num_operations
            elif word1[i] != word2[j]:

                # try swapping 
                swap_operations = 1 + dfs(i + 1, j + 1)

                # try inserting 
                insert_operations = 1 + dfs(i, j + 1)

                # try removing 
                remove_operations = 1 + dfs(i + 1, j)

                min_operations = min(swap_operations, insert_operations, remove_operations)
                memo[(i,j)] = min_operations 

                return min_operations 

            
            # no alteration needed, their equal!
            num_operations = dfs(i + 1, j + 1) 
            memo[(i,j)] = num_operations 
            return num_operations 


        return dfs(0, 0)


