class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            Minimize the number of transformations that are performed 

            Can only transform words if words only differ by exactly one position 

            Early termination if the word is not within the wordList 

            Problem:
                How can we optimize "canTransform"? Are we just going to be subject to an O(k + m) time complexity
                each time, where k is starting word, and m is word to transform into? 

        """

        if endWord not in wordList:
            return 0
        
        # construct patterns 
        patterns_to_word = defaultdict(list)
        words = wordList + [beginWord]

        for word in words:
            
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns_to_word[pattern].append(word)
        
        print(patterns_to_word)
        q = deque([(1, beginWord)]) 
        visited = {beginWord}

        while q:


            depth, curr_word = q.popleft() 
            print(f"Depth: {depth}, Curr Word: {curr_word}")
            if curr_word == endWord:
                return depth 
            
 
            for i in range(len(curr_word)):
                curr_pattern = curr_word[:i] + "*" + curr_word[i + 1:]
                print(f"Curr Pattern: {curr_pattern}")

                # process neighbors that are only 1 change apart
                words = patterns_to_word[curr_pattern]
                print(f"Extracted Words: {words}")
                for word in words:
                    if word not in visited:
                        visited.add(word)
                        q.append([depth + 1, word])


        return 0 