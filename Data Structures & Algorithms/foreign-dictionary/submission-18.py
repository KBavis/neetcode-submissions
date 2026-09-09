class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
            Gaurantees:
                a) The words are sorted in LEXICOGRAPHICAL ORDER 
                        ---> EX) ab && az ---> b will be before z 
                        ---> abc && ab --> this is invalid 
                        
                        NOTE: Dependencies exist once w1 and w2 find differing characters 
            


            1) iterate through words 
            2) we grab a "pairing" of the words (w1 and w2)
            3) we iterate across the min distance of these words while w1_prefix == w2_prefix 
                    --> ensuire the assumption that w1 length < w2 lenght 
            
            4) setup an adjancy list
                    --> dictionary for a set of letters 
                        z: set{o}
            

            5) p --> b 
            6) p --> b --> d 
            7) p --> d 


            topological sort --> DFS and then return reversed order of this 
                    --> vistied set that marks when its compelte versus processing 
            

            return "" when cycle detected 

            iterate across the keys of our adjancy likst 
        """


        # 1) setup the adjancy list 
        adjList = defaultdict(set)
        for i in range(1, len(words), 1):
            w1 = words[i - 1]
            w2 = words[i]

            x = len(w1)
            y = len(w2)
            min_len = min(x, y)
            if w1[:min_len] == w2[:min_len] and x > y:
                return "" 

            for j in range(min_len):
                if w1[j] == w2[j]:
                    continue
                
                adjList[w1[j]].add(w2[j])
                break 
        

        # 2) setup DFS to ensure no cycles and construct solution 
        visited = {c: 0 for word in words for c in word}
        res = []
        def dfs(c):
            if visited[c] == 1:
                return False 
            elif visited[c] == 2:
                return True 
            

            visited[c] = 1 
            for nei in adjList[c]:
                if not dfs(nei):
                    return False 


            visited[c] = 2 
            res.append(c)

            return True 
        

        # 3) invoke DFS and solve problem 
        for c in visited.keys():
            if not dfs(c):
                return "" 
        
        # 4) return expected solution
        return "".join(word for word in reversed(res))
