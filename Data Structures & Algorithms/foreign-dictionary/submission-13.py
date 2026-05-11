class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
            Given list of strings 
            Sorted in lexicographical order 

            Determine order of the letters 


            Conditions:
                - ba
                - bd --> a comes before d 

                - abcdef
                - abcde

            Iterate through words (two seperate pointers)

            Find the min length of two words 

            FInd where they differ

            Once we find where they differ, then a --> b (add to adjancency list)

            Return the order, we iterate through depdnency, append to list

        """

        adjList = {c: set() for w in words for c in w}


        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1] 

            min_len = min(len(w1), len(w2))

            # ensure that sorted lexicogrpahically 
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return "" 
            

            # process and determine dependencies 
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break 
            


        # process and determine if valid   
        res = [] 
        visited = {}
        def dfs(c):
            if c in visited:
                return visited[c] == 2

            visited[c] = 1

            for nei in adjList[c]:
                if not dfs(nei):
                    return False 
                
            visited[c] = 2
            res.append(c)
            return True 


        for key in adjList.keys():
            if not dfs(key):
                return ""
        
        return "".join(reversed(res))

