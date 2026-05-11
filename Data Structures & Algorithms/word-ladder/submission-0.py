class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        min_transforms = self.search(beginWord, set(), wordList, endWord, 1)
        return min_transforms if min_transforms != float('inf') else 0
        
    

    def search(self, currWord, visited, wordList, endWord, count):
        if currWord == endWord:
            print('Found word!')
            return count 
        elif len(visited) == len(wordList):
            return float('inf')
        
        min_transformations = float('inf')
        visited.add(currWord)

        print(f"CurrWord = {currWord}, Visited = {visited}, Count = {count}")

        for next_word in wordList:
            if next_word not in visited and self.canTransform(currWord, next_word, 0, 0):
                print(f'Checking NextWord={next_word}')
                transformations = self.search(next_word, visited.copy(), wordList, endWord, count + 1)
                print(f'Transofmrations={transformations}')
                min_transformations = min(min_transformations, transformations)
        
        return min_transformations
    

    def canTransform(self, w1, w2, i, currTransformations):
        print(f"CanTransform: w1={w1}, w2={w2}, i={i}, currTransformation={currTransformations}")
        if currTransformations > 1:
            return False
        elif w1 == w2:
            return True 
        elif i == len(w1) and i == len(w2):
            return True 
        

        if w1[i] == w2[i]:
            return self.canTransform(w1, w2, i + 1, currTransformations)
        else:
            return self.canTransform(w1, w2, i + 1, currTransformations + 1)