class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        # form the adjancency list 
        adjList = {c: set() for word in words for c in word}

        for i in range(1, len(words)):


            s1 = words[i - 1]
            s2 = words[i]

            minLen = min(len(s1), len(s2))
            if s1[:minLen] == s2[:minLen] and len(s1) > len(s2):
                return ""

            for j in range(minLen):
                
                # found order!
                if s1[j] != s2[j]:
                    adjList[s1[j]].add(s2[j])
                    break
        

        res = []
        visited = {c: 0 for c in adjList.keys()} #0 = not visited, 1 = seen and current path, 2 = finished processed


        # perform post order dfs and form result 
        def dfs(c):
            if visited[c] != 0:
                return visited[c] == 1
            

            visited[c] = 1 
            for nei in adjList[c]:
                if dfs(nei):
                    return True
            
            res.append(c)
            visited[c] = 2 

            return False
        

        for c in adjList:
            if dfs(c):
                return ""
        

        res.reverse()
        return "".join(res)
            




                


