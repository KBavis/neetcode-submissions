class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            a) how to determine if 1 word can be transformed into another word in <= 1 change efficiently 
                - group by pattern (*at --> [bat, sat])
            
            early termination --> endWord not in the wordList 

            pattern: [associated words]

        """
        adjList = defaultdict(list)
        for word in wordList:

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)
            
        q = deque([(beginWord, 1)])
        print(adjList)

        visited = {beginWord}
        while q:

            curr, length = q.popleft()  

            for i in range(len(curr)):
                pattern = curr[:i] + "*" + curr[i + 1:]

                for word in adjList[pattern]:
                    if word == endWord:
                        return length + 1 
                    elif word not in visited:
                        visited.add(word)
                        q.append((word, length + 1))
        
        return 0

