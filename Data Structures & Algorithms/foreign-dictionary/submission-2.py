class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""
        

        # build adjacency lists 
        mapping = {c: set() for word in words for c in word}

        # only account for first difference for determining relative order
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    mapping[w1[j]].add(w2[j])
                    break

        visited = {} # True = in path, False = completed visited
        result = []
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True 
            for nei in mapping[c]:
                if dfs(nei):
                    return True 
            
            result.append(c)
            visited[c] = False 
            return False 
        

        for c in mapping:
            if dfs(c):
                return ""
        
        result.reverse()
        return "".join(result)

        