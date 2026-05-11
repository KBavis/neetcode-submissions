class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        # build adj list 
        adjList = {c: set() for word in words for c in word}

        # s1, s2
        for i in range(0, len(words) - 1, 1):

            s1 = words[i]
            s2 = words[i + 1]

            # get prefix 
            minLen = min(len(s1), len(s2))
            if s1[:minLen] == s2[:minLen] and len(s1) > len(s2):
                return "" 
            
            for j in range(minLen):

                if s1[j] != s2[j]:
                    adjList[s1[j]].add(s2[j])
                    break 
        



        # post order dfs to form solution and perform cycle detection 
        visited = {c: 0 for c in adjList.keys()} 
        res = [] 

        def dfs(c):

            # check if in current path
            if visited[c] == 1:
                return False 
            elif visited[c] == 2:
                return True 
            

            visited[c] = 1 
            for nei in adjList[c]:
                if not dfs(nei):
                    return False 
            
            res.append(c)
            
            visited[c] = 2 
            return True 
        

        # call dfs and return solution 
        for key in adjList.keys():
            if not dfs(key):
                return ""
        
        return "".join(reversed(res))

