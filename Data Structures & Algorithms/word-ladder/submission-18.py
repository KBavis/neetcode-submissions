class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            1) need efficient way to be able to determine if we can map X word in Y word 
                cat --> [bat, sat, fat] --> *at --> [cat, sat, fat, bat]
                leverage the "wildcard" mapping of patterns to associated words 
            
            2) can't transform beginWord to endWord if endWord not in wordList 

            3) BFS (layer by layer) from start word to potential "neighbors" 
                    --> neighbors are all of the words that current word can transform into by single trasnformation 
            
            4) once we've found endWord, return since this is the lowest number of transformations that we can get to word  

            5) shouldn't repeat previously processed words 
        """

        def get_pattern(word, i):
            postfix = word[i + 1:] if i + 1 < len(word) else ""
            curr_pattern = word[:i] + "*" + postfix
            return curr_pattern


        if endWord not in wordList:
            return 0
        elif endWord == beginWord:
            return 0 
        

        # Time: O(n * L^2), Space: O(n * L^2)
        pattern_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern_to_words[get_pattern(word, i)].append(word)
        

        q = deque([beginWord])
        numTransformations = 1 
        seen = {beginWord}

        # queue touches words a single time 
        while q:

            curr_level_length = len(q)
            for i in range(curr_level_length):


                curr_word = q.popleft() 
                if curr_word == endWord:
                    return numTransformations
                

                # iterate through potential patterns 
                for i in range(len(curr_word)):
                    curr_pattern = get_pattern(curr_word, i)
                    
                    # grab neighbors and append to queue if needed 
                    for word in pattern_to_words[curr_pattern]:
                        if word not in seen:
                            q.append(word)
                            seen.add(word)
                    pattern_to_words[curr_pattern] = [] # empty bucket once processed 
            

            # once level ended, number of transformations increases by 1 
            numTransformations += 1 
        
        return 0 
