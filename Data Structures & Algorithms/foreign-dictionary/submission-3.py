class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return "" 

        
        # build adj lists 
        mapping = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # w1 greater in length AND same prefix, then its invalid 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: 
                return "" 
            
            for j in range(minLen):

                # find first differing character between two words and set up dependency (w1 char comes before w2 char)
                if w1[j] != w2[j]:
                    mapping[w1[j]].add(w2[j])
                    break 
                


        visit = {} # False = visited, True = visited AND in current path 
        res = [] 

        # post order dfs!! ensures proper order by processing children first 
        def dfs(c): 
            if c in visit:
                return visit[c]
            

            visit[c] = True 

            for nei in mapping[c]:
                if dfs(nei):
                    return True 
            
            # build result in reverse order 
            res.append(c)

            visit[c] = False 
        

        for c in mapping:
            if dfs(c):
                return "" 
        
        res.reverse() 
        return "".join(res)
