class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Determine  the order to the characters based on passed in words 

        Form an adjacncey list character by character 

        To find dependencies 
        """


        # form adjacency list (ensuring that given rules apply --> if s1 is prefix of s2 and len(s2) < len(s1)


        # mapping {character: set(dependencies)}
        adjList = {c: set() for word in words for c in word}

        for i in range(len(words) - 1): 

            s1 = words[i]
            s2 = words[i + 1] 

            x = len(s1)
            y = len(s2)
            min_length = min(x, y)

            # invalid structure
            if s1[:min_length] == s2[:min_length] and x > y:
                return ""

            # find first occurrence of different letter 
            for j in range(min_length):

                c1 = s1[j]
                c2 = s2[j]

                if c1 != c2:
                    adjList[c1].add(c2)
                    break
                    
        
        result = []

        # form the solution and account for potential cycles 
        visited = {c: 0 for c in adjList.keys()} 

        def dfs(c):
            if visited[c] == 2:
                return True
            elif visited[c] == 1:
                return False
            
            visited[c] = 1

            neighbors = adjList.get(c, [])
            for nei in neighbors:
                if not dfs(nei):
                    return False 
            
            visited[c] = 2
            result.append(c)

            return True
        
        for c in adjList.keys():
            if not dfs(c):
                return ""
        

        return "".join(reversed(result))
