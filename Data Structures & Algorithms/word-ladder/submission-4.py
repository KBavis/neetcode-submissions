class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjList = self.buildAdjList(wordList)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:

            currWord, length = queue.popleft() 

            for i in range(len(currWord)):
                pattern = currWord[:i] + "*" + currWord[i + 1:]


                for nextWord in adjList[pattern]:

                    if nextWord == endWord:
                        return length + 1 
                    elif nextWord not in visited:
                        visited.add(nextWord)
                        queue.append((nextWord, length + 1))
        

        return 0


    def buildAdjList(self, wordList):
        adjList = defaultdict(list)

        for word in wordList: 

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)
        
        return adjList 


