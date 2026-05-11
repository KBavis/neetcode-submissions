class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Create adjacency list for all unique characters
        adj = {c: set() for word in words for c in word}

        # Step 2: Build graph edges based on first different character
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Edge case: invalid dictionary (prefix case)
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:  # FIXED
                    adj[w1[j]].add(w2[j])
                    break  # only first difference matters

        # Step 3: DFS to detect cycles and produce topological order
        visit = {}  # char -> bool (True=cycle, False=visited)
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]  # True means cycle

            visit[c] = True  # mark as visiting
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False  # mark as fully visited
            res.append(c)
            return False

        for c in adj:
            if dfs(c):
                return ""  # cycle detected

        res.reverse()
        return "".join(res)