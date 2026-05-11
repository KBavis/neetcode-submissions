class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        return self.search(beginWord, wordList, endWord)
        
    

    def search(self, currWord, wordList, endWord):
        
        queue = deque([(currWord, 1)])
        visited = {currWord}

        while queue:

            currWord, length = queue.popleft() 
            visited.add(currWord)

            for next_word in wordList:
                if next_word == endWord and self.canTransform(currWord, next_word, 0, 0):
                    return length + 1
                elif next_word not in visited and self.canTransform(currWord, next_word, 0, 0):
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
        
        return 0
    

    def canTransform(self, w1, w2, i, currTransformations):
        print(f"CanTransform: w1={w1}, w2={w2}, i={i}, currTransformation={currTransformations}")
        if currTransformations > 1:
            return False
        elif i == len(w1) and i == len(w2):
            return True 
        

        if w1[i] == w2[i]:
            return self.canTransform(w1, w2, i + 1, currTransformations)
        else:
            return self.canTransform(w1, w2, i + 1, currTransformations + 1)