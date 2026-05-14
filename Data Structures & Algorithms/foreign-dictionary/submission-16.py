class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
            1) Form adjancency list 
                -  z --> o 
                - leverage a dictioanry of set  
                - need s1 and s2 to do comparisons 
                - find first difference in s1 and s2 and setup adjancney list and break 
                - ensure when we find difference, s1 < s2 
            

            2) Itereate through the keys of our adjancny list 
                - call dfs() on that value 
                - add value to visited list 
                - postorder dfs 
            

            3) Reverse the result (topological sort)
                    - if dfs() returns false, a cycyle was found, return "" 
        """

        # 0) Handle edge cases
        if not words:
            return "" 
        elif len(words) == 1:
            return words[0]



        # 1) Form the adjancency list 
        adjList = {c: set() for word in words for c in word}
        for i in range(1, len(words)):

            s1 = words[i - 1]
            s2 = words[i] 
            x = len(s1)
            y = len(s2)

            min_len = min(x,y)
            if s1[:min_len] == s2[:min_len] and x > y:
                return "" 

            for j in range(min_len):

                c1 = s1[j]
                c2 = s2[j]

                # found difference, update the adjanency list
                if c1 != c2:
                    adjList[c1].add(c2)
                    break 
        


        # 2) Configure Post-Order DFS (0=Unseen, 1=Processing, 2=Processed)
        visited = {char: 0 for word in words for char in word}
        res = [] 

        def dfs(c):
            if visited[c] == 2:
                return True 
            elif visited[c] == 1:
                return False 
            
            # mark as visiting 
            visited[c] = 1 

            # process neighbors
            for nei in adjList[c]:
                if not dfs(nei):
                    return False 
            

            # mark as processed and append to result 
            visited[c] = 2 
            res.append(c)

            return True 


        # 3) Invoke Post Order DFS on each potential character
        for c in adjList.keys():
            if not dfs(c):
                return "" 
        

        # 4) Return Back Topologically Sorted Result 
        return "".join(reversed(res))



