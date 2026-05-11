class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        return self.brute_force(text1, text2)


    def brute_force(self, text1: str, text2: str):
        """
        Brute Force Solution: 
                Recurse through (i,j) which are pointers to location in text 
                Have max of two be "final" position 

                abcdefg
                bf
        """

        self.res = 0
        memo = {}
        

        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            elif len(text1) == i or len(text2) == j:
                return 0
            elif i == len(text1) or j == len(text2):
                return 
            

            curr_t1 = text1[i]
            curr_t2 = text2[j]

            # check if they both match 
            if curr_t1 == curr_t2:
                curr = dfs(i + 1, j + 1) + 1
            else:
                curr = max(
                    dfs(i + 1, j),
                    dfs(i, j + 1)
                )
            
            memo[(i,j)] = curr
            return curr
        

        return dfs(0, 0)
            
